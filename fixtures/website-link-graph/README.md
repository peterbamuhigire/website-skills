# website-link-graph fixture

Synthetic built site for `scripts/content_link_graph.py` (M10-11-T11). Expected findings, exactly:

- one orphan page: `orphan.html` (no inbound link; also listed as unreachable from home);
- one broken link: `index.html` links to `contact.html`, which does not exist;
- one missing anchor: `services.html` links to `services.html#faq`, and no element has `id="faq"`.

`about/` resolves to `about/index.html`, and `#visit` and `#prices` resolve, so they are not findings.
