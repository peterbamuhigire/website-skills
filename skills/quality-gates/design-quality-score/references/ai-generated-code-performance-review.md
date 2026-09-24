# AI-Generated Code Performance Review

Parent skill: [design-quality-score](../SKILL.md). Read before merging any
component, page or script drafted by an AI coding assistant (including this
engine's own Claude or Codex output), and when writing the prompt that asks an
assistant to build UI.

AI assistants produce code that usually satisfies the prompt and often misses
the non-functional requirements: speed, accessibility and interface states.
Treat AI output like work from a fast junior developer: read it, measure it,
fix it, then gate it.

## Three review questions

Ask these of every generated component before looking at anything else:

1. **LCP:** does this sit on the critical path or change how the largest
   above-fold element loads?
2. **INP:** does any computation or synchronous work run during render or in an
   input handler?
3. **CLS:** will anything it inserts move content that is already visible?

## Pitfall catalogue

| Pitfall | What to look for | Correction |
|---|---|---|
| Heavy dependency for a small job | Date, charting or utility libraries imported for one function | Native platform APIs or a few lines of code |
| Missing states | No loading, empty or error state | Skeleton matching final geometry; empty message with next action; error with retry |
| Accessibility omissions | Missing alt text, labels, focus management, keyboard paths | Add them; announce async updates with `aria-live` |
| Unsized media | `<img>`/`<iframe>` without dimensions | Width and height or `aspect-ratio` |
| Per-keystroke work | Filtering or sorting on every key press | Debounce, memoise, or commit on submit |
| Outdated APIs | `document.write`, synchronous requests, DOM built from strings of untrusted data | Modern equivalents; safe DOM construction |
| Quadratic work | Nested loops over unbounded data; DOM queries inside loops | Index once; batch reads and writes |
| Lazy hero | `loading="lazy"` on the first image | Eager and `fetchpriority="high"` |
| Blocking scripts | Classic script in `<head>` | `defer` or module |

## Merge checklist

1. Every new dependency is justified in the pull request, or replaced with
   native code.
2. `route-weight-budget` passes for every affected route; record the JS and CSS
   change in KB.
3. `html-perf-lint` passes.
4. LCP: hero is eager, prioritised and sized; no new render-blocking resource.
5. INP: no heavy work in render or input paths.
6. CLS: all media sized; async content has reserved space.
7. States: loading, empty, error (with retry) and success implemented.
8. Accessibility: labels, alt text, focus management, keyboard access, live
   regions for async updates.
9. No O(n²) work on unbounded data; no layout reads inside write loops.
10. Profiled once on the stress profile and once on a real low-cost Android
    phone before release; results recorded.

## Performance-constrained prompt template

Use when asking an assistant to build or change UI. Fill the brackets.

```text
Build [component] for [page template] of a static site built with [framework].
Constraints:
- No new dependencies unless you state why native code cannot do it.
- Route budget: JS <= [N] KB gzip, CSS <= [N] KB gzip for the whole route.
- Do not block the main thread: no heavy work in render or input handlers;
  debounce text input; yield in long loops.
- Reserve space for anything that loads later; give every image and iframe
  width and height; never lazy-load the first image.
- Implement loading, empty, error (with retry) and success states.
- Accessibility: WCAG 2.2 AA; labels, keyboard access, focus management,
  aria-live for async updates.
- Target device: a low-cost Android phone on a slow, high-latency connection.
Return: the code, a list of dependencies (should be none), and how each
constraint is met.
```

Iterate with specific feedback ("the filter runs on every key press; debounce
it and memoise"), never "make it faster". Profile before and after any change
an assistant calls an optimisation; many such suggestions have no measurable
effect.

## Worked example

An assistant drafts an article list that fetches posts and filters by title.
It works, but shows a blank area then a jump, has unsized thumbnails and filters
on every key press. Review fixes: three skeleton cards of final size, an error
message with retry, a 300 ms debounce plus memoised filter, dimensions on all
thumbnails (lazy only below the first card), and a polite live announcement.
Evidence recorded: weight report before and after, lint pass, stress-profile
Lighthouse median, one real-device check.

## Selling point, stated honestly

"We use AI to draft code faster. An engineer reviews and speed-tests every
component before it reaches your customers." Do not claim speed results that
were not measured.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — the "correct but not optimal" model, review questions, merge
  checklist and constraint-led prompting. Studies the book cites about AI code
  quality are not repeated here; verify them at source before quoting.
