# Gap Analysis

## Main System Gaps

### 1. Enforcement Still Lags Behind Guidance

This is now the primary limiter.

The repository has stronger artifacts, better stage gates, and much better operations than
it had before, but too many standards are still enforced socially rather than mechanically.

Examples:

- Lighthouse targets are stated, but not enforced by a hard gate
- QA and rollback standards exist, but are not yet wired into an automated CI pipeline
- accessibility standards are present in multiple places, but there is no dedicated accessibility gate
- strategy and trust requirements are documented, but downstream validation is still light

### 2. Visual QA Is Still Missing

The repo has excellent design thinking, but still lacks a first-class rendered-output review loop.

What is still missing:

- screenshot comparison or screenshot review guidance as an operational gate
- hierarchy and overflow checks on real pages
- a structured method to catch "technically correct, visually weak" output

This matters because premium design quality is judged on the page, not in the reference notes.

### 3. Performance Is Better Framed Than Enforced

Performance discipline is stronger than before, especially after Phase 6, but it is not yet
machine-enforced across the system.

Missing or still weak:

- one canonical performance-gate command
- route-level performance budget enforcement
- CI failure on performance regression
- bundle, image, and JS budget tracking

### 4. Accessibility Is Still Not A First-Class System Skill

Accessibility is respected in the repo, but it still behaves more like a distributed expectation
than a dedicated operating layer.

What remains missing:

- a dedicated accessibility-audit or accessibility-gate skill
- stronger keyboard/focus verification rules in the main launch flow
- more explicit accessibility pass/fail output tied to stage gates

### 5. CI And Automation Are Still Partial

The repository now has:

- QA matrices
- pre-launch checklists
- rollback runbooks
- a Playwright starter

That is real progress. But the engine still lacks a canonical automated CI path at the repository level.

Remaining gap:

- the standards exist, but the repo does not yet guarantee they run automatically and consistently

### 6. Governance Exists, But Has Not Yet Been Proven At Team Scale

Phase 9 added the right governance structures:

- role-based training map
- governance policy
- quality metrics dashboard definition
- maintenance calendar
- agency operations handbook index

This closes the documentation gap.

What remains unproven:

- whether a second or third operator can run the system cleanly in practice
- whether the governance rhythm will actually be maintained
- whether repository reviews will consistently remove drift instead of only documenting it

### 7. Legacy Documentation Drift Is Reduced, But Not Eliminated

The highest-visibility repo-level drift has now been cleaned up, especially in the top-level
documentation. The remaining gap is narrower and now sits mostly in older legacy references
and long-tail supporting docs rather than in the primary entry points.

What still remains:

- some older reference files still carry dated framing
- a few supporting docs still overlap in scope or terminology
- some capabilities are better documented than they are mechanically enforced

This is no longer a top-level coherence problem, but it still warrants periodic cleanup.

## What Has Been Closed Since The Earlier Evaluation

These were real weaknesses before and are materially better now:

- intake and qualification are now structured
- strategy is now a first-class artifact rather than an implied activity
- launch and rollback are now documented system behavior
- post-launch review exists as an operating standard
- governance and onboarding are now explicit
- the repo is less founder-dependent than before

## Bottom-Line Limiters

The main blockers preventing a true world-class score today are:

- insufficient hard validation
- missing visual QA
- incomplete accessibility enforcement
- incomplete CI integration
- limited proof that the governance model works under multi-operator conditions
