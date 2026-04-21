---
name: spotpaper
description: Read a paper draft or research repo for an empirical social-science paper project and turn its core argument into a dataviz-based visual concept. Use this when the user wants a visual concept, dataviz direction, poster concept, visual brief, or mechanism-based visual grammar for a paper draft, manuscript, or research repository.
---

# SpotPaper

Use this skill when the user wants to turn an empirical paper project into a clear visual concept.

This skill is for:

- paper drafts
- manuscript folders
- research repos
- requests for paper visuals, poster concepts, dataviz marks, or visual briefs

This skill is not for:

- generic logo generation unrelated to the paper's argument
- decorative illustration-first work
- purely theoretical papers with no empirical anchor

## Core Behavior

SpotPaper should:

1. read the most decision-relevant paper material available
2. identify the paper's core visualizable argument
3. choose the most suitable visual grammar
4. produce a usable visual brief
5. when the case is clearly Python-first, produce a concrete Python draft plan and, if requested or obviously useful, generate a first plotting script
6. after generating a visual draft, review the image before treating it as acceptable output
7. run a naive-reader check through an isolated sub-agent that sees only the image itself, not the paper background
8. triage the findings into layout problems versus interpretation problems
9. revise layout or semantic clarity as needed, then rerun the image once or twice before stopping
10. do not stop just because the image is understandable; stop only when both interpretation and layout quality clear the bar

The output should help the user decide what to make, not just how to style it.

## Input Rules

Assume the user may provide either:

- a paper draft
- a research repo

Do not assume the title and abstract are the only inputs.

When the input is a repo, treat it as a paper project rather than a generic codebase. Prioritize:

1. draft files, manuscript files, and paper text
2. abstract, introduction, conclusion, and results sections
3. figures, tables, captions, and output artifacts that reveal the main contrast
4. notes, memos, slides, and README-style descriptions
5. code only when it helps identify the empirical structure or mechanism

## Numeric Fidelity

Do not invent numeric series, intermediate points, proportions, or time paths for dataviz drafts.

If a figure depends on quantitative geometry, such as:

- time-series values
- bar heights or widths
- area encodings
- precise relative positions
- multi-year trajectories

then use one of these sources only:

1. original data from the user
2. a research repo containing the underlying code or outputs
3. values that can be carefully read from the paper's own tables or figures

If none of these are available, stop and ask the user for the data or repo instead of fabricating a schematic numeric path.

It is acceptable to produce:

- a non-numeric conceptual brief
- a wireframe-like layout plan without quantitative claims

It is not acceptable to draw a pseudo-quantitative chart that could be mistaken for the paper's actual empirical result.

## Evidence Modes

When a user wants a quantitative draft, choose one of these evidence modes before drawing:

### 1. Data-Grounded Redraw

Use this when you have:

- user-provided data
- a research repo with plotting code
- exported regression or figure data

This is the preferred mode.

### 2. Figure-Grounded Redraw

Use this when you do not have raw data, but the paper's own figure or table is clear enough to serve as the evidence source.

In this mode:

- preserve the paper figure's structure and reported relationships
- redraw the visual cleanly instead of pasting the raw screenshot into the output
- use only what can be responsibly read from the figure, table, or caption

Do not silently invent missing intermediate values.

### 3. Composite Fallback

Use this only when:

- the paper figure is the only trustworthy numeric evidence available
- a faithful redraw is not feasible in the current turn

In this mode:

- keep the paper figure as evidence
- isolate it clearly as a source panel
- add SpotPaper interpretation around it

This is a fallback, not the preferred path.

### 4. Stop And Ask

If neither data-grounded nor figure-grounded work is feasible, stop and ask the user for:

- the repo
- exported figure data
- the original plotting script

Do not push forward with a pseudo-quantitative draft.

## Required Reading

Before producing the final answer, read:

- [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md)

Read [README.md](README.md) only if you need the product framing or want to check the intended output contract.

## Output Contract

Return the result in these four required sections:

### Paper Essence

- One-sentence claim
- Core mechanism
- Main contrast
- Key result
- Tone

### Visual Recommendation

- Minimal causal sentence
- Candidate visual grammars
- Best visual grammar
- Why it fits

### Main Visual Sentence

- One sentence only

### Draft Brief

- Recommended artifact
- Layout concept
- Key numbers to retain
- What to emphasize
- What to avoid
- Python-first recommendation

When Python-first is clearly recommended and the user wants the skill to go further, add a fifth section:

### Python Draft Plan

- Chart structure
- Required numeric inputs
- Proposed encodings
- Script output target
- Implementation notes

If the user asks for an actual draft, create a Python script under `scripts/` or another suitable workspace path instead of stopping at the plan.

When a quantitative draft is attempted, also add:

### Evidence Mode

- Selected mode
- Evidence source
- Why this mode was chosen
- Numeric fidelity risk

If the selected mode is figure-grounded, you may also add:

### Figure-Grounded Redraw

- Source figure or table
- What was preserved
- What was redrawn
- What remains approximate

After a visual draft has been generated, add:

### Image Review

- Verdict: `pass`, `pass_with_minor_issues`, or `needs_revision`
- Main issues
- Recommended revisions

Treat this as a layout-and-presentation gate, not a generic comment section.
Do not mark the image as effectively done if any of these remain material:

- a crowded plot area
- legend or annotations competing with the main data
- weak information hierarchy
- cramped cards, labels, or metric blocks
- footer or attribution competing with content
- a layout that still looks like a working draft rather than a presentation-quality figure

Do not place workflow-status or evidence-mode language in the main title area of the figure.
Phrases such as `repo data redraw`, `figure-grounded redraw`, `composite fallback`, or `reported effects below` belong in the external writeup, generation log, or a compact source note, not in the figure's headline region.
When a draft image is generated, prefer to store this explanatory material in an English `README.md` placed in the same artifact directory as the script and image.
That `README.md` should carry the provenance and process notes so the figure itself can stay clean.
For presentation-style figures intended to be read quickly, do not place a source note inside the figure body or footer.
Keep provenance in the sidecar `README.md` unless the user explicitly asks for an in-figure source line.

Do not assume a generated image is acceptable without reviewing it.

After image review, add:

### Naive Reader Review

- Perceived message
- Likely misreadings
- Clarity blockers

This check should be done from the perspective of a reader who sees only the image.
Do not feed the paper abstract, the correct interpretation, or the intended main visual sentence into this check.
When possible, execute this check with a fresh sub-agent or isolated thread that does not inherit the full conversation history.

If the verdict is `needs_revision` or `pass_with_minor_issues`, you may add:

### Revision Triage

- Layout problems
- Interpretation problems
- Chosen revision path

Use this section to decide whether the next revision should target presentation or meaning.

If interpretation problems are material, you may add:

### Semantic Revision

- Meaning problem
- Changes made
- Re-render target
- Re-review result

Use semantic revision to clarify the message without changing the paper's underlying claim.
Typical fixes include defining ambiguous labels, clarifying the mechanism, and marking study-specific estimates or scope.

If layout problems are material, you may add:

### Layout Revision

- Revision focus
- Changes made
- Re-render target
- Re-review result

Use layout revision to fix presentation problems, not to change the paper's core visual logic.
Default to at most two revision rounds unless the user asks for deeper polishing.

Do not stop the layout loop merely because there is no overlap.
Continue revising if the figure is still visually crowded, hierarchically flat, or obviously workmanlike.

Only stop layout iteration when one of these is true:

1. `Image Review = pass`
2. `Image Review = pass_with_minor_issues`, and the remaining issues are genuinely cosmetic rather than structural
3. the maximum revision rounds have been used, in which case report residual layout issues explicitly

## Working Style

- Visualize the argument, not just the topic.
- Draw structure, not abstract nouns.
- Keep one dominant visual sentence.
- Prefer explanation over decoration.
- Use numbers selectively.
- Prefer semantic axes when the point is directional meaning rather than precise numeric read-off.
- For abstract continuous measures like similarity, stability, reweighting, exposure, uncertainty, or attention, reduce dense ticks and use semantic endpoints or `higher/lower = ...` cues when appropriate.
- Use color and symbol language to show hierarchy, not decorative variety.
- When multiple series appear, explicitly decide which is `primary`, which are `secondary`, and which are `reference`.
- If one series carries the core message, make it dominant and demote the others with lighter color, thinner weight, or dashed treatment.
- Do not mechanically color-match unrelated layers, such as top-panel metrics and bottom-panel logic cards, unless they truly represent the same variable or category.
- Keep symbol meaning stable within one figure: stronger line for primary series, muted line for reference series, shaded bands for periods, arrows for summary linkage rather than automatic causality.
- Recommend Python-first drafting when proportions or composition logic matter.
- When generating a Python draft, prefer simple, editable `matplotlib` code over clever abstractions.
- Numeric plots must be grounded in actual paper values, extracted figure values, or repo data. Do not interpolate a believable-looking series from prose descriptions alone.
- If raw data is unavailable but the paper figure is usable, prefer a figure-grounded redraw over directly embedding a noisy screenshot.
- Use composite fallback only when a clean redraw is not feasible in the current turn.
- When a draft image exists, inspect it and review layout quality before calling it done.
- When a draft image exists, test whether a naive reader can understand the intended message from the image alone, preferably via an isolated sub-agent with no paper background.
- Triage failures into layout problems and interpretation problems before revising.
- If the issue is presentation, revise layout first.
- If the issue is understanding, revise semantic clarity without changing the core empirical claim.
- Do not place workflow labels such as `Python-first draft` inside the main image area.
- If attribution is needed, use a very small, light-gray `generated by SpotPaper` credit in a bottom-right whitespace area that does not collide with the main content or footnotes.
- When image artifacts are saved, write an English `README.md` in the same folder to capture evidence mode, sources, redraw scope, review outcome, and open issues.
- For quick-read presentation figures, keep provenance out of the figure itself and in the sidecar `README.md` instead.

If the paper is too abstract, too diffuse, or not empirically anchored enough for a strong dataviz concept, say so clearly and recommend a more restrained direction.
