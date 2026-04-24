# SpotPaper Draft Notes

## Artifact

- Paper: `From Rhetoric to Regime: Policy Transitions in China`
- Draft directory: `writing/StateCap_policy_dynamics/spotpaper_draft`
- Current Python-rendered source artifact:
  - `current/statecap_transition_story.py`
  - `current/statecap_transition_story.png`
  - `current/statecap_transition_story_thumbnail.png`
- Current Image2 polished presentation artifact:
  - `current/statecap_transition_story_polish.png`
  - `current/statecap_transition_story_polish_thumbnail.png`
- Snapshot preserved before the 2026-04-24 redraw:
  - `snapshots/20260424_074639_statecap_transition_story.py`
  - `snapshots/20260424_074639_statecap_transition_story.png`
- Snapshot preserved before the Image2 polish pass:
  - `snapshots/20260424_080408_statecap_transition_story_before_image2.png`
- Older files in this directory should be treated as superseded prototypes:
  - `statecap_regime_draft.py/.png`
  - `statecap_regime_composite.py/.png`
  - `statecap_regime_redraw.py/.png`

## Evidence Mode

- Selected mode: `data_grounded_redraw`
- Why this mode was chosen:
  - the repo contains the transition-series data needed for the upper panel
  - the repo also contains paper tables with reported firm-level estimates for the lower panel
- Numeric fidelity standard:
  - no hand-invented time path
  - no screenshot-based reuse of the full paper figure as the final visual panel

## Sources

### Upper panel

- Data file:
  - `data/term_ts_aggregates.csv`
- Series used:
  - `reset_intensity = 1 - js_sim`
  - This is equivalent to normalized Jensen-Shannon transition intensity from the repo aggregate series.

### Lower panel

- Reported estimates drawn from:
  - `writing/StateCap_policy_dynamics/tables/2_EPU_firm_realizedvol.tex`
  - `writing/StateCap_policy_dynamics/tables/2_EPU_policy_discussion.tex`
  - `writing/StateCap_policy_dynamics/tables/2_EPU_firm_soe.tex`

### Paper text used for interpretation

- Manuscript source:
  - `writing/StateCap_policy_dynamics/1_main.tex`

## What Was Redrawn

- Redrawn directly from repo data:
  - the adjacent-year policy-language reset intensity time series in the top panel
- Redrawn as paper-grounded summary cards:
  - the reported market-volatility response
  - the reported disclosure-response estimates
  - the ownership heterogeneity note highlighting stronger non-SOE response

The lower panel is a structured summary of reported paper results, not a raw regression table and not a direct paper-figure crop. The stable-versus-transition similarity benchmarks are kept in `PAPER_TAKEAWAYS.md` rather than shown in the main reading path.

## 2026-04-24 Refresh

- Main semantic change:
  - the upper panel now plots transition intensity (`1 - js_sim`) instead of similarity, so higher values visually mean a larger policy-language reset
- Layout changes:
  - collapsed the two large context boxes into one evidence-base line
  - kept a single dominant time-series panel and two consequence cards
  - removed in-plot y-axis endpoint labels after they competed with the line in the left corner
- Thumbnail check:
  - saved to `current/statecap_transition_story_thumbnail.png`
  - first-glance message recovered: policy-language resets are measured over time and linked to higher volatility plus later disclosure among exposed firms
- Current verdict:
  - `Image Review`: `pass_with_minor_issues`
  - `10-Second Read Check`: `pass`
  - `Naive Reader Review`: `pass_with_minor_issues`
- Residual issues:
  - a reader still needs the paper or notes to understand the exact construction of firm exposure and normalized JS transition intensity
  - the early-series high reset value is data-grounded but may draw attention away from the shaded post-handoff windows

## Review Summary

### Maker review

- The newest version applies a stricter figure budget: one context strip, one dominant chart, and two consequence cards.
- The chart now carries the reset logic directly, so there is no separate narrative-reset card competing with it.
- Coefficients and benchmark chips have been removed from the main reading path.
- The latest pass also moves event and metric explanation into the chart subtitle and removes the connector arrow between result cards.

### Naive reader review

A blind-style review was run from the image and thumbnail only, without using additional paper context during the read itself. The review recovered the main message:

- policy-language continuity changes over time
- breaks cluster around political transitions and shocks
- those breaks are linked to market volatility and later disclosure responses

The review also surfaced the remaining risks:

- some paper-internal phrasing still leaked into the figure, especially `paper benchmark` and unexplained significance stars
- the connector arrows can still be read as either sequence or causality, so wording has to do the disambiguation work
- the figure is now readable and presentable, but still a presentation graphic rather than a finished poster panel

### 10-second read check

A thumbnail artifact is now saved alongside the main figure:

- `current/statecap_transition_story_thumbnail.png`

The thumbnail-based quick-read check surfaced this pattern:

- first-glance message: political handoffs interrupt an otherwise smoother policy-language path, and the lower cards translate that interruption into firm outcomes
- what drew attention first: the headline, then the blue line and the colored metric cards
- what still competes mildly with the main message: the chip row is useful but still gives the eye a second destination before the chart
- what improved in the final pass: the benchmark numbers no longer fight the plot, the right-side summary lane is gone, and the title area now breathes

## Revision Triage

- Layout problems:
  - minor only; the main structure is already stable
- Interpretation problems:
  - `paper benchmark` is too manuscript-internal
  - significance stars read like unexplained notation
  - some labels still require too much paper context
- Chosen revision path:
  - semantic revision first, with no major layout change

## Semantic Revision

- Meaning problem:
  - the figure was directionally readable, but a naive reader could not decode the benchmark chip or the coefficient notation cleanly
- Changes made:
  - changed `Paper benchmark` to `Reported averages`
  - changed `stable` / `transition` to `steady years` / `reset years`
  - rewrote the top panel in plain language as year-to-year policy-language continuity
  - demoted numeric coefficients from the main card headline to supporting lines
- Re-render target:
  - `current/statecap_transition_story.png`
- Re-review result:
  - a fresh blind review recovered the core message cleanly but still found method-facing terms harder to decode

## Final Blind Review

- Perceived message:
  - political leadership changes reorder policy language, which then affects firms through volatility and later disclosure changes
- What still confused the blind reader:
  - the exact metric behind the line chart and the role of the shaded windows and dashed markers
  - whether the two result cards should be read as causal claims or as reported patterns
- What remained uninterpretable:
  - how the paper measures exposure and language units without opening the paper
  - the exact practical meaning of the underlying line metric beyond the plain-language cue

## Latest Blind Review

- Perceived message:
  - political leadership changes reshape policy language before firms visibly adjust, and more exposed firms show stronger market volatility and later policy discussion
- What still confused the blind reader:
  - the exact meaning of the top chart's y-axis
  - whether `smaller change` and `bigger reset` are labels of size, direction, or importance
- What remained uninterpretable:
  - how `policy documents`, `recurring terms`, and `more exposed firms` are defined
  - what the dashed event markers mean beyond `major events`

## Sub-agent Checks Used In This Run

- `019db48c-c3ce-79c2-9198-5f08a71632ec`
  - thumbnail-only 10-second read check
- `019db48d-4220-7ab2-8d11-3a0dcd48f347`
  - first full-image naive-reader review after the stricter-budget redraw
- `019db48e-510f-7981-a68c-a680e908e0e6`
  - final full-image naive-reader review after the last semantic wording pass
- `019db4d2-82bc-76f1-91bf-9743a665bd7a`
  - thumbnail-only 10-second read check for the newest simplified redraw
- `019db4d3-0f47-7e10-9448-4da525234e32`
  - full-image naive-reader review for the newest simplified redraw

## Open Issues

- If this is promoted to a still cleaner keynote asset, the context strip can be reduced to one line of small text rather than three boxes.
- If this is promoted to a paper-adjacent poster, add a separate companion panel for term substitution rather than pushing more method detail into this figure.
- If the figure is used in a manuscript, keep provenance and evidence-mode notes in sidecar documentation rather than in the image.

## Final Verdict

- `Image Review`: `pass_with_minor_issues`
- `10-Second Read Check`: `pass`
- `Naive Reader Review`: `pass_with_minor_issues`

The SpotPaper cycle is complete for this draft. The main claim now reads correctly for a blind reviewer, and the remaining issues are semantic rather than structural: a non-paper reader still cannot decode the underlying metric or measurement logic from the figure alone.

## Usage Note

Per the current SpotPaper rule set, explanatory process text should live in this `README.md`, not inside the main figure headline area.

## 2026-04-24 Image2 Polish Pass

- Mode:
  - image-to-image polish only; no structural Python redraw
- Input:
  - `current/statecap_transition_story.png`
- Output artifacts:
  - `current/statecap_transition_story_polish.png`
  - `current/statecap_transition_story_polish_thumbnail.png`
- Changes applied:
  - lightened and smoothed the background
  - softened card fills, card borders, gridlines, and reset-window bands
  - sharpened the blue time-series line and markers
  - made event labels quieter and cleaner
  - tightened the visual rhythm between title, evidence line, chart, and cards
- Review result:
  - the polished variant reads cleaner and more presentation-ready than the Python source image
  - all main text, data geometry, and the two-card structure were preserved
  - no new metrics, icons, source notes, or decorative elements were added
- Residual issues:
  - the polish output is `1536x1024`, so it is a separate presentation variant rather than a replacement for the 4:3 Python-rendered source
  - exact measurement construction still belongs in the paper or sidecar notes, not inside the figure

## Historical Image2 Polish Pass

- Mode:
  - image-to-image polish only; no structural Python redraw
- Input:
  - `current/statecap_transition_story.png`
- Output artifacts:
  - `current/statecap_transition_story_image2.png`
  - `current/statecap_transition_story_image2_thumbnail.png`
  - `current/statecap_transition_story.png` (updated to the polished version)
  - `current/statecap_transition_story_thumbnail.png` (updated to the polished version)
- Changes applied:
  - shortened the subtitle to `China, 2003-2022`
  - reduced the visual weight of the two top context strips
  - tightened chart-title spacing
  - lightened gridlines and event markers
  - increased the crispness of the blue line
  - softened the bottom card fills and borders
  - preserved all wording, data geometry, and labels
- Blind-review result:
  - the polished version reads faster at a glance and the central chart now dominates more clearly
  - remaining issues are mild top-heaviness and the still-abstract `stable` / `transitioning` axis language
- Follow-up:
  - a second lighter polish pass was attempted but cancelled after the image model stalled
  - this pass is now superseded by the 2026-04-24 Python redraw
