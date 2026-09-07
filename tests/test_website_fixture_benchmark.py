import json
import subprocess
import sys
import shutil
import pytest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fixture_copy(tmp_path):
    target = tmp_path / "site"
    shutil.copytree(ROOT / "fixtures/website-kaizen", target)
    return target


def run_fixture(path):
    command = [sys.executable, str(ROOT / "scripts/website_fixture_benchmark.py"), "--fixture", str(path)]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return result.returncode, json.loads(result.stdout)


@pytest.mark.parametrize('pages', [[], None, ['../outside.html'], ['index.html', './index.html'], [False]])
def test_invalid_page_catalogue_fails(tmp_path, pages):
    site = fixture_copy(tmp_path)
    config = json.loads((site / 'fixture.json').read_text(encoding='utf-8'))
    config['pages'] = pages
    (site / 'fixture.json').write_text(json.dumps(config), encoding='utf-8')
    code, result = run_fixture(site)
    assert code == 1
    assert result['status'] == 'FAIL'


def test_metadata_failure_blocks_aggregate(tmp_path):
    site = fixture_copy(tmp_path)
    page = site / 'index.html'
    text = page.read_text(encoding='utf-8').replace('name="description"', 'name="removed-description"')
    page.write_text(text, encoding='utf-8')
    code, result = run_fixture(site)
    assert result['pages'][0]['metadata']['status'] == 'FAIL'
    assert code == 1 and result['status'] == 'FAIL'


def test_nested_assets_are_counted(tmp_path):
    site = fixture_copy(tmp_path)
    (site / 'assets').mkdir()
    (site / 'assets' / 'large.bin').write_bytes(b'x' * (1024 * 1024))
    code, result = run_fixture(site)
    assert code == 1
    assert result['performance_budget_inputs']['status'] == 'FAIL'


def test_negative_and_boolean_budgets_are_not_numeric_limits(tmp_path):
    from scripts.website_fixture_benchmark import run_benchmark
    for value in (-1, True, '100'):
        budgets = {'global': {'total_weight_kb': value, 'js_kb_gzip': 0, 'css_kb_gzip': 0}}
        path = tmp_path / 'budgets.json'
        path.write_text(json.dumps(budgets), encoding='utf-8')
        with pytest.raises(ValueError, match='non-negative'):
            run_benchmark(ROOT / 'fixtures/website-kaizen', path)


@pytest.mark.parametrize('field,value', [
    ('total_weight_kb', 10**400),
    ('js_kb_gzip', 10**400),
    ('css_kb_gzip', 10**400),
    ('total_weight_kb', 1e308),
], ids=['huge-total-integer', 'huge-js-integer', 'huge-css-integer', 'total-float-overflow'])
def test_overflowing_budgets_return_structured_failure(tmp_path, field, value):
    budgets = json.loads((ROOT / 'performance-budgets.json').read_text(encoding='utf-8'))
    budgets['global'][field] = value
    path = tmp_path / 'budgets.json'
    path.write_text(json.dumps(budgets), encoding='utf-8')
    result = subprocess.run(
        [sys.executable, '-B', '-X', 'utf8', str(ROOT / 'scripts/website_fixture_benchmark.py'),
         '--budgets', str(path)], cwd=ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    output = json.loads(result.stdout)
    assert output['status'] == 'FAIL'
    assert 'numeric conversion range' in output['error']
    assert output['evidence_type'] == 'lab fixture only'
    assert 'Traceback' not in result.stderr


@pytest.mark.parametrize('delta,expected', [(0, 'PASS'), (-1, 'FAIL'), (1, 'PASS')])
def test_raw_byte_budget_boundary(tmp_path, delta, expected):
    from scripts.website_fixture_benchmark import run_benchmark

    site = fixture_copy(tmp_path)
    before = {path: path.read_bytes() for path in site.rglob('*') if path.is_file()}
    size = sum(len(data) for path, data in before.items() if path.name != 'fixture.json')
    budgets = {'global': {'total_weight_kb': (size + delta) / 1024,
                          'js_kb_gzip': 80, 'css_kb_gzip': 30}}
    path = tmp_path / 'budgets.json'
    path.write_text(json.dumps(budgets), encoding='utf-8')
    result = run_benchmark(site, path)
    assert result['status'] == expected
    assert result['performance_budget_inputs']['status'] == expected
    assert all(path.read_bytes() == data for path, data in before.items())


@pytest.mark.parametrize('field', ['title', 'description'])
@pytest.mark.parametrize('value', ['', ' \t\n', '&nbsp;'])
def test_blank_metadata_blocks_aggregate(tmp_path, field, value):
    site = fixture_copy(tmp_path)
    page = site / 'index.html'
    original = 'Kaizen fixture — home' if field == 'title' else 'Fictional local fixture for deterministic website checks.'
    text = page.read_text(encoding='utf-8')
    assert original in text
    page.write_text(text.replace(original, value), encoding='utf-8')
    code, result = run_fixture(site)
    assert result['pages'][0]['metadata']['status'] == 'FAIL'
    assert code == 1 and result['status'] == 'FAIL'


def test_title_comment_and_body_text_do_not_supply_title(tmp_path):
    site = fixture_copy(tmp_path)
    page = site / 'index.html'
    text = page.read_text(encoding='utf-8').replace('Kaizen fixture — home', '<!-- Not title text -->')
    page.write_text(text, encoding='utf-8')
    code, result = run_fixture(site)
    assert result['pages'][0]['metadata']['status'] == 'FAIL'
    assert code == 1 and result['status'] == 'FAIL'


def test_title_text_across_parser_chunks_and_padded_description_pass(tmp_path):
    site = fixture_copy(tmp_path)
    page = site / 'index.html'
    text = page.read_text(encoding='utf-8').replace('Kaizen fixture — home', ' Home <!-- split --> &amp; about ')
    text = text.replace('Fictional local fixture for deterministic website checks.', '  Fixture description.  ')
    page.write_text(text, encoding='utf-8')
    code, result = run_fixture(site)
    assert result['pages'][0]['metadata']['status'] == 'PASS'
    assert code == 0 and result['status'] == 'PASS'


def test_local_website_fixture_benchmark_is_deterministic():
    command = [sys.executable, str(ROOT / "scripts/website_fixture_benchmark.py")]
    first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    assert json.loads(first.stdout) == json.loads(second.stdout)
    result = json.loads(first.stdout)
    assert result["status"] == "PASS"
    assert result["evidence_type"] == "lab fixture only"
    assert result["field_core_web_vitals"] == "NOT ASSESSED"
