# SpotPaper

SpotPaper is a product for turning the core argument of an empirical paper project into a clear, dataviz-based visual concept.

It is designed for cases where a paper has a strong empirical claim, but the mechanism or contrast is hard to communicate quickly to non-specialists. SpotPaper helps identify what should be visualized, which visual grammar fits best, and what a first draft should emphasize.

## Product Purpose

SpotPaper helps researchers, designers, and research teams move from:

- a paper draft or research repo

to:

- a clear visual direction that is faithful to the paper
- a recommended dataviz grammar
- a concise visual sentence
- a draft brief that can be used for design or prototyping

The product is not meant to replace final visual design. Its purpose is to improve the quality of visual decisions at the concept stage.

## Target Use Cases

SpotPaper is best suited for:

- empirical social-science papers
- economics, finance, political economy, public policy, and adjacent fields
- papers with a clear main finding
- papers where a contrast, mechanism, or channel can be visually structured

Typical use cases include:

- creating a visual concept for a paper-based poster
- designing a dataviz-style mark for a paper summary
- preparing a visual brief before drafting a figure or graphic
- translating a draft paper or research repo into a communication-ready visual idea

## Non-Target Use Cases

SpotPaper is not optimized for:

- purely theoretical papers
- papers without a clear empirical result
- generic branding or logo generation unrelated to the paper's argument
- illustration-first tasks where style matters more than analytic structure

## Product Approach

SpotPaper does not try to literally illustrate abstract academic concepts such as incentives, expectations, selection, or coordination.

Instead, it converts them into visual structure.

The product typically works with visual grammars such as:

- flow
- gate
- funnel
- prism
- split
- divergence
- layered mechanism
- composition shift

The main objective is to visualize the argument, not just the topic.

## Inputs

### Primary Input

SpotPaper is intended to work from one of these sources:

- a paper draft
- a research repo

### What SpotPaper Looks For

From that input, SpotPaper extracts the material needed to identify the visualizable argument, such as:

- title
- abstract
- introduction
- results sections
- figures or tables
- notes about the intended audience or output

### Optional

- preferred output type: `mark`, `poster`, `banner`, or `auto`
- user notes

## Outputs

SpotPaper V1 returns four structured outputs after reading the draft or repo context.

### 1. Paper Essence

A compressed reading of the paper, including:

- one-sentence claim
- core mechanism
- main contrast
- key result

### 2. Visual Recommendation

A recommendation for the most appropriate visual grammar, with a short explanation of why it fits the paper.

### 3. Main Visual Sentence

A single sentence describing what the final visual should communicate.

This is the central output of the workflow.

### 4. Draft Brief

A concrete draft direction, including:

- suggested layout
- key numbers to retain
- what to emphasize
- what to avoid
- whether a Python-first dataviz draft is recommended

## Recommended Workflow

In the standard workflow:

1. SpotPaper reads the paper draft or repo and identifies the core visualizable argument.
2. SpotPaper recommends a visual grammar and produces a draft brief.
3. A first draft is created, often in Python if structure and proportions matter.
4. The draft is later refined into a poster, mark, banner, or other visual asset.

## When Python-First Drafting Is Recommended

SpotPaper should recommend a Python-first draft when the visual depends on:

- real proportions
- strong empirical contrasts
- area or width encoding
- careful layout logic

This is especially important when the intended output behaves more like a compressed data visualization than a stylized illustration.

## Example

For a paper draft or repo arguing that industrial policy shapes IPO access in China, SpotPaper may produce:

- Paper Essence: policy changes who enters the IPO pipeline
- Visual Recommendation: use a gate, prism, or composition-shift structure
- Main Visual Sentence: favored industries occupy a much larger share of IPO access than their baseline economic share
- Draft Brief: compare GDP share, IPO gate selection, and IPO share in one vertically structured dataviz mark

## Product Principles

SpotPaper follows these product principles:

- visualize the argument, not just the topic
- draw structure, not abstract nouns
- keep one dominant visual sentence
- use key numbers selectively
- prefer clarity over decoration
- avoid cliché academic imagery unless it clearly improves comprehension

## Version Scope

SpotPaper is currently a V1 product.

V1 focuses on:

- identifying the right visualizable argument
- selecting a suitable visual grammar
- producing a usable draft brief

V1 does not aim to fully automate polished final graphics.

## Short Description

SpotPaper turns a paper draft or research repo into a clear dataviz-based visual concept centered on the paper's core mechanism and key result.
