# Infographics and Explanatory Visuals on Websites

Parent skill: [design-system](../SKILL.md). Read when a page carries an infographic, process or
lifecycle diagram, timeline, comparison graphic, map, social card, or a downloadable poster, deck or
report. For a plain chart or table, use `data-tables-charts-and-svg-rules.md`.

Related files: `enterprise-data-viz-rules.md` (dashboards), `math-for-web-design.md` (proportion).

The full rule set is the Chwezi Infographics Design and Production Quality Standard, which lives in
the `chwezi-design-engine` engine (`doctrine/infographics-standard.md` and the skill
`chwezi-infographics-standard`). Resolve its location from the engine-routing table; never assume a
path. This file keeps the website-specific working rules in original words. When the two differ,
the engine's text wins and its checker (`scripts/check_infographic.py`) is the measuring tool.

---

## 1. Facts first

1. **One takeaway, one audience.** Write the single sentence the visual must teach before any art.
   If the story does not fit legibly on a phone, make a series, not smaller type.
2. **Every number has a source.** Keep a small register beside the asset: claim, exact wording on the
   graphic, source, publication and retrieval date, period, unit, denominator, calculation. A figure
   without an entry is removed or labelled "illustrative" on the graphic itself.
3. **Never invent.** No plausible-looking percentages, rankings, citations, client logos, awards or
   testimonials to fill space. Illustrative data is flagged where the reader sees it.

## 2. Honest encodings

1. Bars start at zero; line scales are honest and labelled; no 3D or perspective effects.
2. Check the **lie factor**: (effect shown in the graphic) / (effect in the data), where effect =
   |second - first| / first. Accept 0.95 to 1.05. A bar axis starting at 3,200,000 for values
   3,200,000 and 3,400,000 turns a 6% gap into an apparent 100% change (about 16 times too large).
3. **Area follows value.** A circle's radius scales with the square root of the value; doubling the
   radius quadruples the area (lie factor 3). Pictogram counts equal the data.
4. Shares that must total 100% use largest-remainder rounding (floor each, give the spare points to
   the largest fractional parts): 41.4 / 33.3 / 25.3 shows as 42 / 33 / 25, not 41 / 33 / 25.
5. Do not sum quantities in different units. Percent and percentage points are never mixed.
6. **Maps** only when location is the evidence: title, legend, scale or "not to scale", boundary and
   base-map source with date and licence, boundaries current for the date shown, and shaded values
   as rates against a stated denominator (per 1,000 people), not raw counts. Web Mercator multiplies
   areas by 1 / cos^2(latitude), about 1.33 at 30 degrees and 4.0 at 60 degrees: use an equal-area
   projection when comparing areas across a continent.

## 3. Structure that is true

1. Keep process, cycle and hierarchy diagrams as data (nodes and edges). Check for duplicate or
   orphan steps, unreachable steps, unlabelled decision branches, a loop drawn as a chain, a cycle
   with no entry point, and numbers that disagree with the real order. The engine's checker does this
   in seconds and writes the text equivalent from the same data.
2. Use a cycle only for a genuinely recurring process; mark the entry point and one direction.
3. Timelines use a true time scale when duration matters; otherwise label them "sequence, not to
   scale".
4. Comparisons apply the same criteria to every option, with "N/A" shown, not silently dropped.

## 4. Text and imagery

1. **Real text only.** Set labels as live text (HTML or SVG `<text>`) in the site's fonts. Text baked
   into a generated image, warped lettering or invented glyphs is a release blocker. If a generator
   garbles words, redraw the layout with real text over clean artwork.
2. **No synthetic photorealism.** Do not use generated photorealistic people, offices, clinics or
   sites as if they were real. Use client or licensed photographs, or clearly illustrative vector,
   isometric or editorial art. Never present a synthetic image as proof or as a testimonial.
3. Keep the illustration layer separate from the text layer so copy can change without redrawing.
4. Logos and partner marks are real, current, permitted and unaltered.

## 5. Build for the web

1. Prefer inline or `<img>` SVG with a `viewBox`, explicit dimensions, grouped semantic layers and
   no external dependencies. PNG or WebP is an export, not the master.
2. Wrap the graphic in `<figure>` with a visible `<figcaption>` carrying the source and date.
3. Give it a short text alternative (what it is and the takeaway) and a **long text equivalent** (a
   list or table of the same facts, in reading order) that is on the page or linked from the figure.
   Complex images need both; support for individual ARIA techniques varies by browser and assistive
   technology pair, so test with a real screen reader and record the result (current support matrix:
   NOT_ASSESSED).
4. Never carry meaning by colour alone; pair status with a label, icon or pattern. Check contrast
   for text and meaningful graphics against the repository's WCAG 2.2 AA target.
5. Reflow: the graphic reorders, not shrinks, on a narrow screen. Test 320 CSS px wide and large
   system text; if a diagram cannot reflow, provide the stacked or tabular alternative.
6. **Phone canvas scale for social and share cards.** Text on the canvas must be the minimum CSS
   size times (canvas width / displayed width): a 1,080 px card shown in a 360 px slot is scaled
   by 3, so 16 CSS px body text needs 48 px on the canvas. Proof it on a real phone, after platform
   compression, without zoom. Platform crop sizes change; measure before each campaign.
7. Performance: optimise and minify SVG without dropping `title`, `desc` or ids; lazy-load below the
   fold; set width and height to avoid layout shift; keep the page within its route weight budget.

## 6. Downloads (posters, decks, reports)

1. Offer the PDF as a second route, never the only one: the same facts exist in HTML.
2. Screen PDF: selectable text, bookmarks, document title and language. Print file: agreed bleed,
   embedded fonts, colour profile and effective resolution (about 3438 / viewing distance in inches
   pixels per inch; roughly 90 ppi at 1 m, 290 ppi at 0.3 m); proof at actual size.
3. Text size from the reading distance on posters: about 23.6 pt per metre at print size.
4. A deck or report placed on a page is linked with its date, version and owner; a superseded file
   is marked and redirected, never silently overwritten.

## 7. Release checklist

- [ ] Takeaway sentence and source register exist; every figure is traceable or flagged.
- [ ] Lie factor and area scaling checked; maps normalised; totals reconcile.
- [ ] Diagram data passed the structure checker; text equivalent generated and reviewed.
- [ ] Live text, no pseudo-text, no synthetic photorealistic people or fake logos.
- [ ] Short alt text, long equivalent, contrast and non-colour cues verified.
- [ ] Rendered at 320 px, tablet and desktop widths, with large text; social cards proofed on a phone.
- [ ] Downloads have an HTML counterpart and a version note.

## Sources

- Chwezi Core Systems (2026) *Chwezi Infographics Design and Production Quality Standard*, version
  1.0.0, in `chwezi-design-engine`; read 2026-11-08 (internal standard; review with the engine).
- Edward R. Tufte (1983, 2nd ed. 2001) *The Visual Display of Quantitative Information*, Graphics
  Press (lie factor; durable concept).
- W3C WAI (n.d.) *Complex Images* tutorial, https://www.w3.org/WAI/tutorials/images/complex/
  (short and long text alternatives); live page not read on 2026-11-08, so the exact current
  wording is NOT_ASSESSED; review by 2027-02-08.
