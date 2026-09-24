# Data Tables, Charts and SVG Rules

Parent skill: [design-system](../SKILL.md). Read when a website page shows a table, chart, statistic panel or hand-built SVG graphic (pricing comparisons, results tables, impact dashboards, annual-report pages), or when reviewing chart or SVG code for correctness.

Related files: `enterprise-data-viz-rules.md` (dashboard hard rules, pre-attentive attributes, chart-type mapping). Full implementation walkthroughs, D3 patterns and runnable skeletons live in the design engine: `C:/wamp64/www/design-system-skills/skills/12-data-viz-and-dashboards/data-visualization/references/svg-css-js-implementation.md` and `chart-encoding.md`.

---

## 1. Chart rules

1. **Readability first.** A chart must be understood without effort; remove ornament that does not encode data.
2. **No 3D effects.** Perspective distorts comparison.
3. **Grid lines** connect marks to axis values; keep them light and few.
4. **Legend** whenever there is more than one series; label lines directly where possible.
5. **Tooltips** add detail but never carry essential information; the chart must work without hover (touch and keyboard users). Offer the same values in a table or text.
6. **Colour:** distinguishable hues with adequate contrast between series and against the background; never colour alone to separate series.
7. **Real data only.** Design with representative real values; placeholder data hides structural problems (label lengths, outliers, empty categories).
8. **Sorting:** for bar and column charts of categories, sort by value or offer ascending/descending controls.
9. **Accessible SVG:** `role="img"`, a `<title>` and `<desc>` (or `aria-labelledby`), and respect `prefers-reduced-motion` for animated entries.

---

## 2. Table rules

| Content | Alignment |
|---|---|
| Text | Left |
| Numbers, currency, percentages | Right, with consistent decimal places and tabular figures |
| Icons, status badges | Centre |

- Headers align with their column content.
- Give rows comfortable height; cramped rows slow reading.
- Paginate long tables (or "load more") and keep the page size predictable.
- Add sortable headers with a visible sort indicator, a search box and filters for large sets; persist filter state in the URL where results are shareable.
- Keep the header row sticky when the table scrolls.
- Use zebra striping only for dense tables where row tracking is hard; add full vertical and horizontal rules only for very complex grids, as heavy rules slow scanning.
- On small screens, either allow horizontal scroll with the first column pinned or reflow each row into a labelled card; never shrink text below the body minimum.

---

## 3. SVG correctness checklist

Use this when writing or reviewing hand-coded SVG charts or icons.

- [ ] Origin is top-left; y increases downward. Invert scales for values that grow upward.
- [ ] Circles and ellipses are positioned with `cx`/`cy` (and `r`, `rx`, `ry`), not `x`/`y`.
- [ ] `fill` and `stroke` are set explicitly; defaults (black fill, no visible stroke) surprise.
- [ ] Path commands: uppercase letters use absolute coordinates, lowercase relative (`M`, `L`, `C`, `Q`, `A`, `Z`).
- [ ] Transform lists are read as successive changes to the coordinate system from left to right, which is equivalent to applying them to the shape from right to left; check the order when combining `translate` and `rotate`.
- [ ] Elements created in script use `document.createElementNS('http://www.w3.org/2000/svg', …)`; plain `createElement` produces non-rendering elements.
- [ ] Measure SVG shapes with `getBBox()` (user units); `getBoundingClientRect()` returns screen pixels after transforms.
- [ ] Responsive sizing uses `viewBox` with CSS width and height; control scaling with `preserveAspectRatio` (CSS `object-fit` does not apply to inline SVG).
- [ ] Data joins use array methods deliberately: `map` to transform, `filter` to subset, `reduce` to aggregate, `forEach` only for side effects.
- [ ] Charts redraw on container resize (`ResizeObserver`) rather than on window width alone.

---

## Sources

- Elisa Paduraru (2024) *Roots of UI/UX Design: Learn to Develop Intuitive Web Experiences*, Creative Tim (charts and tables).
- Peter Cook (2022) *Fundamentals of HTML, SVG, CSS and JavaScript for Data Visualisation*, Leanpub.
- *DESIGN.RIP — Master UI Design Elements* (table spacing, alignment, sticky headers and filtering); publication details as available in the source file.
