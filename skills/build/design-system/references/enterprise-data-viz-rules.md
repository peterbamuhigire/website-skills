# Enterprise Data Visualisation Rules

Parent skill: [design-system](../SKILL.md). Read when a project includes dashboards, reports or public data pages, including those built through the dashboards engine. Related detail: `data-tables-charts-and-svg-rules.md`.

## Principle

The purpose of a chart is to improve understanding, not to decorate. Choose the chart type for the data and the question it answers, never for the look of the dashboard.

## Hard rules for premium dashboards

- No 3D charts of any kind. Use flat pie, bar and line forms.
- No heavy shadows or gradients on chart marks; they distort the perception of size and quantity.
- Use colour to add meaning (emphasis, focus, category), never as decoration.
- Give each figure enough context (axis, unit, period, comparison) for the reader to interpret it.

## Pre-attentive attributes

The eye registers these before conscious attention. Use them deliberately to direct the reader.

| Attribute | Use for |
|---|---|
| Size | Quantity, weight, importance |
| Colour difference | Categories; status (red, amber and green sparingly, and never as the only signal) |
| Orientation | Direction of trend |
| Proximity | Grouping related items |
| Similarity or difference | Same shape for same kind, different shape for different kind |
| Connection | Relationships between points (lines, links) |

## Chart choice by data type

| Data | Suitable chart |
|---|---|
| Composition (whole and parts) | Stacked bar with few categories (five or fewer); avoid pie beyond about four slices |
| Comparison across categories | Horizontal or vertical bar |
| Change over time | Line |
| Distribution | Histogram or box plot |
| Correlation | Scatter plot |
| Geography | Choropleth or simple map |
| Hierarchy | Treemap, only when depth is three levels or fewer |

## Anti-patterns that fail design review

- Pie chart with more than four slices
- Any 3D pie
- Bars with gradient fills
- Line chart with more than about seven series on one axis
- Donut with a centre figure unrelated to the chart total
- Speedometer gauges on analytical dashboards
- Colour used for decoration, not meaning
- One colour carrying two categorical meanings on the same screen

## Application by audience

- **Internal back-office dashboards:** efficiency before appearance; density is acceptable if hierarchy is clear.
- **Executive dashboards:** fewer charts, more summary figures, one headline indicator per screen.
- **Public data pages** (marketing, transparency reports): the same rules apply; do not add 3D or gradients to look attractive. Example: a UGX budget-execution page for a district council uses flat bars and a clear table.

## Sources

- Synechron Inc. (2018) *Bridge the User Experience Gap in Enterprise Applications for Financial Services & Insurance*, Synechron. Informed the data-visualisation principles for enterprise interfaces; rules and thresholds here are the engine's own working set and should be tested on each project.
