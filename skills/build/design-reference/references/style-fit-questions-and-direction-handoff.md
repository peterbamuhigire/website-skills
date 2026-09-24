# Style-Fit Questions and Art-Direction Handoff

Parent skill: [design-reference](../SKILL.md). Read when turning reference
sites and discovery answers into a style direction, when a client asks for a
"modern" or "trendy" look without reasons, or when a premium engagement needs
several direction options.

This file supplies the **questions** and the **website-side decisions**. The
art-direction vocabulary (named routes, theme intensity, direction boards and
the fit/stretch/bold options method) is owned by the `design-system-skills`
engine, skill `art-direction-routes`; resolve its location from the global
engine-routing table and do not duplicate it here.

## Style-fit questions (add to the style-fit gate)

Ask these before any route is proposed. Record answers in the style thesis.

1. **Audience and belief.** Who must trust this site, and what should they
   believe within the first screen?
2. **Stigma or expectation to overcome.** What does this audience already
   assume about businesses like this one ("banks are cold", "government is
   opaque", "imported is better", "clinics are expensive")? Which visual
   direction closes that gap?
3. **Real personality.** Does the direction match the client's actual work,
   scale and manner? A style that overpromises is a promise the client must
   keep. Small firms should look like confident small firms, not like an
   agency of fifty.
4. **Job urgency.** How task-critical is the visit? The more urgent the task
   (paying, booking, reporting a problem), the lower the theme intensity.
5. **Mobile job map.** What do phone visitors come to do (call, WhatsApp,
   directions, price check, pay by mobile money, opening hours, download a
   profile)? The mobile hierarchy follows these jobs, not the desktop sitemap.
6. **Maintenance reality.** Who will change text, images and pages after
   launch, and with what skills? Styles that bake text into images or need a
   designer for every change fail this question.
7. **Content reality.** Does the client have the photography, illustration,
   words and update cadence the style needs?
8. **Environment.** Will the style stay inside the performance budget on a
   low-cost Android phone over mobile data?

Style thesis template:

> For [audience] who expect [assumption], this site uses [direction] because it
> signals [belief] from the first screen. It keeps [familiar anchors] where
> people expect them, avoids [misfit], and proves fit through [evidence].

## Unusual layouts: the "method behind it" test

Before any atypical layout or navigation goes to the client:

1. Does it serve the site's purpose, or only the designer's creativity?
2. Which familiar anchors stay intact (logo position, main navigation, primary
   action)?
3. Can a first-time visitor find their way without instructions?
4. Is there a sound small-screen version (a different mobile arrangement is
   acceptable)?
5. Never experiment in checkout, booking or payment flows.

Content-led structures that pass this test more often: map-first interfaces
when location decides the choice (property, tourism, branch finders);
equal-size tile grids for many similar items; a one-page sales pitch for a
single conversion, with the same primary action in every section.

## Trend-adoption questions

For any fashionable treatment (texture, ribbon, glow, carousel, device mock-up,
decorative motion):

1. What does it mean here, and does it connect with this brand's message?
2. Is it decoration only? If so, is decoration the right place to spend budget?
3. Would the design fail without it?
4. How widely is it already used, and will it look dated in two or three years?
5. Can it be done subtly?
6. What does it cost to build and to maintain?
7. Record adopt, adapt or reject with the reason.

Treatments to avoid as defaults (dated surface styles): letterpress inset text,
corner ribbons, zigzag edges, stitched-fabric or literal wood-grain panels,
"hands holding the content", glossy glows, decorative device photographs,
auto-rotating hero carousels and whole-site horizontal scrolling. Any of these
may be revived deliberately when a real brand reason exists; record it.

## Build and maintenance cost flags

Tag each proposed style element so the client chooses knowingly:

| Element | Build | Maintain | Note |
|---|---|---|---|
| Solid colour, type-led, minimal layouts | Low | Low | Code-rendered; fast; editable |
| Very clean layouts | Low–Medium | Low | Depend on careful detail |
| Hand-drawn accents | Medium | Medium | Use a handwriting font for editable text, never hand-lettered headings |
| Layered collage, textures, photographic backgrounds | Medium–High | Medium | Heavier pages; rights and refresh needed |
| Custom form control skins | Medium–High | Medium | Style containers; keep native controls |
| Heavy scripted animation | High | High | Needs a static baseline and reduced-motion path |
| Atypical navigation | High (risk) | Medium | Justify with user evidence |
| Commissioned illustration system | Medium–High | Medium | Needs a style guide for future pieces |
| Art-directed long-form pieces | High per piece | High | Reserve for flagship content |

## Borrow map (inspiration without copying)

1. Gather at least three references per element type (header, navigation,
   hero, proof, footer), including at least one strong regional reference.
2. For each, write one line: "Useful because it solves [problem] by
   [technique]."
3. Map each technique to a wireframe element.
4. Unify with one type system, one colour logic and one spacing scale.
5. Check the result against each source: it must not look like a replica.

Hand the borrow map to the client with the direction; it demonstrates craft and
answers "did you copy X?" before it is asked.

## Handoff to design-system-skills

| Handed over | Artefact | Owner after handoff |
|---|---|---|
| Style-fit answers, style thesis, mobile job map, cost flags, borrow map | `docs/design-reference.md` | design-system-skills `art-direction-routes` builds route options and direction boards |
| Chosen route and the owner's decision | Owner decision register (website-builder) | `design-system` (tokens) and `page-builder` (templates) in this engine |

For a premium discovery tier, offer three direction options (fit, stretch,
bold) through `art-direction-routes`, built from the client's real headline and
photography; price the direction boards as a paid discovery deliverable.

## Sources

- McNeil, P. (2010) *The Web Designer's Idea Book, Volume 2*, HOW Books —
  inspiration-without-copying method, style-to-audience reasoning,
  implementation-cost notes. (A file supplied as the "Mobile Web Designer's
  Idea Book" was in fact this Volume 2.)
- McNeil, P. (2013) *The Web Designer's Idea Book, Volume 3*, HOW Books —
  unusual-layout test, trend-adoption cautions, content-led structures,
  mobile-specific-when-the-job-differs rule, site-type lessons.
