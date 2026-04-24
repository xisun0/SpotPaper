# Paper Takeaways

## Main argument
Political cycles and major shocks trigger abrupt reweighting in China's official policy language, and firms exposed to those narrative transitions face higher uncertainty and then adjust their own policy-facing disclosures.

## Core mechanism
The state communicates governing priorities through standardized policy terms. Most years this narrative mix changes gradually, but National Congress cycles and shock years create discrete regime reordering. That reordering reaches firms unevenly through exposure-weighted policy language, showing up first in volatility and then in subsequent disclosure.

## Key numbers
- Adjacent-year regime similarity is about 0.85 in stable periods and about 0.65 in transition years.
- The corpus covers 67,546 policy documents from 2002 to 2022 and yields 2,247 policy terms.
- The current figure plots normalized reset intensity from the repo series, using `1 - js_sim` from `data/term_ts_aggregates.csv`.
- The realized-volatility coefficient is about 7.98 in the baseline specification, which the manuscript summarizes as roughly a 0.04 SD increase in volatility for a 1 SD shock increase.
- Lagged policy-regime shocks raise later policy discussion, with the disclosure response concentrated among non-SOEs.

## Candidate highlights
- The time path of the Policy Regime Transition Index with political-cycle breakpoints.
- A term-reweighting motif showing old slogans fading while new ones rise.
- The exposed-firm volatility response.
- The follow-on disclosure response in the next period.
- The non-SOE versus SOE contrast in disclosure adjustment.

## Selected highlights for figure
- Argument-led headline: policy-language resets travel into firms.
- One dominant structure: a single transition-intensity time-series panel, where higher values mean more reweighting across policy terms.
- One context strip: corpus scale and language-unit count only.
- One support layer: two firm-consequence cards, with only the economically readable effect size and ownership contrast kept in the main reading path.
- One transmission layer: higher-exposure firms face higher contemporaneous volatility.
- One downstream layer: disclosure expands later, especially for non-SOEs.

## Figure budget selection
- Required in this figure:
  - the transition-intensity time path
  - one plain-language cue for how to read the line
  - two downstream firm consequences
- Deferred to later versions or sidecar notes:
  - stable-versus-reset average numbers
  - regression coefficients and stars
  - any method label beyond a plain-language cue
  - secondary firm-side numbers that are harder to read than a simple economic magnitude
- Excluded from this figure because they widen scope without sharpening the claim:
  - a separate step card for the narrative reset
  - multiple support chips competing with the chart
  - detailed regression notation

## Excluded from this figure and why
- Stable-versus-reset benchmark chip: true but not necessary once the line and shaded reset windows do the work.
- Displayed coefficients on cards: useful for documentation, but they slow the first read.
- Multiple firm-side numbers: not needed once one card already carries an economically legible magnitude.
- Policy-method terminology: better kept in sidecar notes than on the figure surface.

## Deferred highlights
- Full method detail on Jensen-Shannon decomposition.
- The multi-metric robustness comparison across cosine, Pearson, and JS similarity.
- Fine-grained term examples beyond one or two emblematic narrative substitutions.

## Figure-selection rationale
The most useful SpotPaper direction is still not a method diagram or a multi-panel dashboard. The paper's communicative edge is a single visual sentence: political handoff or shock -> policy-language reset -> firm consequences. This version therefore treats the transition-intensity chart itself as the narrative-reset layer, keeps only one evidence-base line, and reduces the support layer to two firm-consequence cards.

## 2026-04-24 SpotPaper refresh
- The preferred figure is now a Python-rendered redraw rather than the earlier image-to-image polish pass.
- The upper panel now encodes reset intensity directly as `1 - js_sim`, so upward movement means more policy-language reweighting.
- The context chips were collapsed into one evidence-base line, and the lower result cards were retained as the only support layer.
- Image review verdict: pass with minor issues; the main remaining caveat is that exact measurement details still require the paper or README.
