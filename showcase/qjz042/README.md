# qjz042 — SpotPaper Draft Log

## Evidence Mode

- Selected mode: `figure_grounded_redraw`
- Evidence source: reported values and tract-level findings stated in the paper text extracted from `qjz042.pdf`
- Why this mode was chosen: the paper provides several exact, high-salience magnitudes that support a faithful quick-read redraw without inventing trajectories
- Numeric fidelity risk: low for the displayed values, moderate if the figure were expanded into curves or maps without extracting additional figure data

## Figure-Grounded Redraw

- Source figure or table: paper text and discussion of the main results in the introduction and tract-level sections
- What was preserved: the reported male-female contrast, the near-universality of tract-level gaps, and the rarity profile of low-gap neighborhoods
- What was redrawn: the paper findings were converted into a single quick-read presentation figure rather than reproduced as the original academic figures
- What remains approximate: the neighborhood-profile pills summarize the qualitative pattern and are not proportional encodings

## Iteration History

- Initial draft exposed three layout failures: overlong headline, row text colliding with bars, and support-card overflow.
- Revision 1 shortened the headline, separated the row labels from the bars, and reduced the support-card copy.
- Revision 2 simplified the semantic labels and compressed the lower-right card.
- Revision 3 tightened the headline to improve the thumbnail read.

## Image Review

- Verdict: `pass_with_minor_issues`
- Main issues:
  - The lower support cards are readable at full size but remain secondary at thumbnail scale, as intended.
  - The lower-right card is denser than the main comparison and should not be made more prominent without risking message competition.
- Recommended revisions:
  - If a presentation deck needs more projection-distance legibility, enlarge the lower card copy slightly or convert the lower-right pills into a single short line.

## 10-Second Read Check

- Items noticed: headline, large `−10` bar for black men, small `+1` bar for black women, `99%`, `<5%`
- Messages perceived: the mobility gap is concentrated among black men; the gap persists in most places; the neighborhoods where it narrows are rare
- Main message: black-white mobility differences are mostly a black-male problem
- What drew attention first: headline, then the long orange bar
- Verdict: `pass`

## Naive Reader Review

- Perceived message: black men have much worse intergenerational outcomes than comparable white men, black women do not show the same gap, and neighborhood exceptions are scarce
- What confused you: the `99%` card needs to be read to recover that it refers to Census tracts rather than people
- What you could not interpret: nothing material at full size
- Verdict: `pass_with_minor_issues`

## Revision Triage

- Layout problems: headline length, annotation overlap, support-card overflow
- Interpretation problems: the first draft made the persistence claim weaker than intended because the lower support layer was visually noisy
- Chosen revision path: simplify headline and row labels first, then reduce the lower-right card to a short rarity claim with three qualitative cues

## Final Layout Check

- Global grid alignment: `pass`
- Title block alignment: `pass`
- Main panel and support-block alignment: `pass`
- Card or metric block consistency: `pass_with_minor_issues`
- Connector alignment: `pass`
- Final verdict: `pass_with_minor_issues`

## IMAGE2 Polish

- Type of polish applied: `structure_polish`, `typography_polish`, `visual_polish`
- Model path used: direct `v1/images/edits` call with `gpt-image-2` via a local dependency-free wrapper, because the bundled helper was missing `openai` and `python-dotenv`
- Output artifact: `current/qjz042_spotpaper_polish.png`

### What Changed

- Tightened the headline and subtitle styling so the main claim reads more like a finished slide than a draft.
- Softened the support-card borders and made the lower support layer quieter.
- Increased card padding and improved the spacing rhythm in the lower half.
- Refined the pill treatment so the three neighborhood cues read more like subtle tags.
- Smoothed bar-label alignment and overall whitespace balance.

### Result Review

- Main message clearer: `yes`
- Structural problems introduced: `no`
- Full-size verdict: `pass`
- Thumbnail verdict: `pass_with_minor_issues`
- Residual issue: the lower-right tags are intentionally quiet and remain small at thumbnail scale, but they no longer compete with the main comparison.
