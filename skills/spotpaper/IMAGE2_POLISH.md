# IMAGE2 Polish

This file defines the optional polish stage for SpotPaper figures.

It is separate from the default SpotPaper workflow on purpose.

## Trigger Rule

Do not enter this polish workflow by default.

Only use it when the user explicitly asks for a second-stage visual refinement step, for example by saying:

- `use image2`
- `polish this figure`
- `make it presentation-grade`
- `do a visual refinement pass`

If the user does not explicitly ask for polish, stop at the normal SpotPaper draft/review cycle.

## Stage Type

This is an image-to-image stage.

The input is a reviewed image file produced by the main SpotPaper workflow.
This stage does not return to Python code or re-render from a script.

If a structural problem is found that cannot be resolved at the image level, flag it explicitly and stop rather than silently switching back to code.

## Prerequisites

Do not enter this stage unless all of the following are true:

- the figure has completed the main SpotPaper review cycle
- `Image Review` or `Final Layout Check` returned `pass` or `pass_with_minor_issues`
- the current reviewed image file path is known and available

## Purpose

The goal of `image2` polish is not to redesign the figure's argument.

It is for improving a figure that is already:

- structurally correct
- evidence-grounded
- scoped correctly
- reviewed for interpretation

This stage should make the figure cleaner, sharper, and more presentation-ready without widening scope or adding extra messages.

## Order Of Operations

Polish should proceed in this order:

1. `structure_polish`
2. `typography_polish`
3. `visual_polish`

Do not jump directly to colors or decorative styling if the figure still has structural or layout problems.

## 1. Structure Polish

First remove or reduce anything that makes the figure feel like a working draft.

Typical structure-polish actions:

- cut non-essential cards, strips, or support blocks
- simplify crowded support rows
- reduce competing secondary metrics
- remove connector text that is not helping
- tighten scope if the figure is trying to say too much
- simplify or shorten overly explanatory subtitles

Questions to ask:

- Does the figure still have only one dominant message?
- Has any support layer turned into a second figure?
- Is every visible block necessary for this version of the figure?

## 2. Typography Polish

After the structure is clean, refine the text system.

Typical typography-polish actions:

- rebalance title, subtitle, and support text sizes
- strengthen or soften type hierarchy
- tighten long labels
- normalize line spacing and card padding
- reduce note-like text
- improve contrast between primary and secondary text
- keep panel-bound text inside its own subplot when feasible

Questions to ask:

- Is the title sharp and readable at a glance?
- Are the key numbers clearly subordinate or dominant in the right places?
- Do labels read like figure language rather than memo language?

## 3. Visual Polish

Only after the structure and type are stable should visual styling be refined.

Typical visual-polish actions:

- tighten the palette
- reduce unnecessary border weight
- refine arrow and connector styling
- harmonize background and panel treatment
- improve whitespace rhythm
- make support layers feel intentionally quieter

Questions to ask:

- Does the figure feel presentation-grade rather than draft-like?
- Is the visual language consistent across panels?
- Has polish improved the figure without adding decorative noise?

## Execution

After completing the three-step analysis, execute the polish in this order:

### 1. Compile the edit prompt

Merge all findings from structure, typography, and visual polish into a single, concrete English prompt.

Rules:
- Use action verbs: `remove`, `soften`, `reduce`, `replace`, `lighten`
- Only describe what to change, not what to keep
- Always append: "Preserve the small 'powered by SpotPaper' attribution in the bottom-right corner."
- Keep it under 200 words

### 2. Snapshot the current image

Before generating, copy the current image to `snapshots/` with a timestamp:

```bash
cp current/<figure>.png snapshots/$(date +%Y%m%d_%H%M%S)_<figure>.png
```

### 3. Call GPT Image 2 edit

```bash
python3 <skill-root>/scripts/image2_edit.py \
  -i current/<figure>.png \
  -o current/<figure>_polish.png \
  -p "<compiled edit prompt>"
```

`<skill-root>` is the root directory of this skill repo — the directory containing this file and `SKILL.md`. In Claude Code it is `$CLAUDE_PLUGIN_ROOT`; in Codex it is resolved by the skill installer. Claude should infer the full path from where it loaded this file.

The output is always a new file. The input image is never overwritten.

Output naming convention: append `_polish` to the original stem.
Example: `rf2023_spotpaper.png` → `rf2023_spotpaper_polish.png`

Do not overwrite the original Python-generated figure. The `_polish` file is a separate artifact and should remain distinct from the main figure.

Requires `OPENAI_API_KEY` in environment or `~/.env`.

### 4. Generate thumbnail

```bash
sips -Z 320 current/<figure>_polish.png --out current/<figure>_polish_thumbnail.png
```

### 5. Review the result

Read the output image and confirm:
- The intended changes were applied
- No new structural problems were introduced
- The main message is clearer than before

Report any residual issues.

## Guardrails

During polish:

- do not widen the figure's scope
- do not add new support metrics unless the user explicitly asks
- do not add process text into the figure
- do not undo the figure budget
- do not sacrifice numeric fidelity for style
- do not let polish create a second headline

## Output

If this stage is used, report:

- what type of polish was applied
- what was changed
- whether the main message became clearer
- any remaining residual issues

## Relationship To SpotPaper

`IMAGE2_POLISH.md` is a second-stage refinement layer.

The normal SpotPaper workflow should:

- read the paper or repo
- choose the figure argument
- build the draft
- review and revise it to a sound version

Only after that should `image2` polish be considered.
