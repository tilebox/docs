---
name: creating-documentation-graphics
description: Creates clean technical graphics for Tilebox documentation. Use for architecture diagrams, flow diagrams, class relationships, trees, graphs, dependency diagrams, and Tilebox workflow diagrams for docs.tilebox.com.
---

# Creating Documentation Graphics

Create clean, technical graphics for the Tilebox documentation website. Use this skill for diagrams and visual explanations that belong in `docs.tilebox.com`, including architecture diagrams, data flows, class relationships, trees, graph structures, dependency diagrams, and Tilebox workflow diagrams.

This skill is derived from the Tilebox infographic style, but it is optimized for documentation: precise, legible, attractive, and easy to drop into Mintlify pages.

## Core rule: start with painter PNGs

When the user asks to create, edit, change, redraw, mock up, or iterate on a documentation graphic, use painter from the start and produce PNG image files. Do not draft the graphic as SVG, Mermaid, D2, HTML, hand-authored vector markup, or another intermediate format and then convert it. Do not only describe the change. Produce updated image files.

If the user asks for a non-visual plan, outline, or copy only, answer normally. But once the task involves visuals or visual edits, use painter.

The only exception is when the user explicitly asks for a Tilebox workflow DAG diagram, a D2 workflow diagram, or to update an existing workflow DAG under `assets/workflows/diagrams/`. In that case, use the existing D2 workflow generator and palette. This exception is only for task/DAG diagrams, not for normal workflow concept, architecture, release, deployment, or data-flow graphics.

## Core outcome

Produce documentation graphics that:

- explain a concrete technical relationship or process;
- fit naturally inside Mintlify pages;
- have matching light and dark variants by default;
- are generated as PNGs with painter by default;
- use a clean technical Tilebox look
- avoid background texture, use a solid color matching the specified documentation background colors for the light/dark theme;
- avoid logos, marketing copy, and presentation-specific decoration.

## Output modes

Always start out with creating a light mode, and afterwards ask the user for confirmation to also generate the dark mode.
When asked to integrate the graphic into the documentation page, always generate both light and dark mode.

Use painter-generated PNG outputs by default:

- `name-light.png`
- `name-dark.png`

Create the light version first, then create the dark version as a color-only edit of the light version. Preserve layout and content exactly.

Only use SVG outputs for the explicit Tilebox workflow DAG / D2 exception. In that case, follow the existing `name.svg` and `name.dark.svg` workflow convention. Do not choose SVGs because they seem easier to maintain; for documentation graphics, the expected artifact is the painter PNG pair.

## Documentation integration pattern

Use the docs repository light/dark image pattern:

```mdx
<img src="/assets/path/example-light.png" alt="Short descriptive alt text" className="dark:hidden" />
<img src="/assets/path/example-dark.png" alt="Short descriptive alt text" className="hidden dark:block" />
```

For the explicit workflow DAG / D2 exception, use the existing SVG pattern:

```mdx
<img src="/assets/workflows/diagrams/svg/example.svg" alt="Short descriptive alt text" className="dark:hidden" />
<img src="/assets/workflows/diagrams/svg/example.dark.svg" alt="Short descriptive alt text" className="hidden dark:block" />
```

Always include meaningful `alt` text. Keep it factual and concise.

## What this skill creates

Use this skill for:

- architecture diagrams;
- service and module interaction diagrams;
- request, event, and data flow diagrams;
- class and object relationship overviews;
- task graphs, DAGs, trees, and dependency graphs;
- state machines and lifecycle diagrams;
- storage, dataset, and workflow mental models;
- small technical visual explainers embedded in guides or concept pages.

Do not include:

- Tilebox logos;
- logo-derived marks used as decoration;
- slide titles or slide-like framing;
- conclusion strips or takeaway banners;
- section numbers;
- footer treatments;
- large marketing headlines inside the image.

Do not use heavy, full-canvas, or central background patterns.

Documentation graphics never need the Tilebox logo. Do not place it in generated graphics.

## Visual style

Use the reference style in `references/best-practice-technical-sketch.jpeg` as the best-practice visual target for normal documentation graphics. It is a clean technical sketch style: thin dark outlines, white or near-background fills, simple line icons, generous whitespace, restrained red action accents, and subtle low-contrast background motifs.

Use the following Tilebox color language and shape language:

- clean, technical, calm, and highly legible;
- polished painter-generated diagrams with a subtle hand-drawn or field-notes feel, similar to the best-practice reference image;
- restrained deep rose accents, default `#BE123C`, used mainly for action arrows, small icon highlights, checks, emphasis marks, and short underlines;
- faint background, matching the to the docs background colors;
- generous whitespace and clear hierarchy;
- short labels close to the things they describe;
- simple arrows and connectors with unambiguous direction, drawn as clean sketch-like strokes with open arrowheads where appropriate;
- iconography: use minimal black line-art icons with tiny red highlights only when they clarify a node or concept;
- consistent spacing, alignment, and shape language;
- prefer white or near-background cards with thin dark borders over colored filled cards;
- use rounded rectangles for actors, systems, and grouped lists, and hexagons for loop steps or lifecycle states when that improves clarity;
- avoid heavy shadows; if needed, use only soft sketch shadows that do not make the graphic look like generic SaaS vector art.

Avoid:

- generic corporate vector art;
- noisy decoration;
- overusing accent colors or filling large cards with red, blue, or gray;
- overdoing iconography;
- playful or childish marker style;
- cursive or handwriting-style fonts;
- tiny labels;
- dense paragraphs inside diagrams;
- low-contrast strokes or fills;
- bulky app-icon style illustrations;
- gradients, glassmorphism, or glossy depth effects.

## Typography

Use Geist as the default font.

Use `Geist Mono` where it helps identify technical terms, code-like labels, identifiers, field names, method names, task names, dataset names, state values, or small snippets.

Examples that should usually use `Geist Mono`:

- `Task`, `Runner`, `Dataset`, `Collection` when shown as code-like entities;
- `job.id`, `collection_name`, `time_interval`;
- method names such as `submit()` or `query()`;
- task class names such as `DownloadTask`;
- state values such as `queued`, `running`, `computed`.

Keep text in graphics short. Prefer one-to-three-word labels and compact identifiers.

## Default color palettes


### Light mode

Use these colors by default for non-workflow documentation graphics:

- **Background:** transparent or `#fcf9fa` only. If using texture, keep the base background exactly `#fcf9fa` and add only subtle low-contrast patterning on top.
- **Primary accent:** `#BE123C` deep rose for active paths, arrows, highlights, emphasis strokes, selected nodes, and small icon fills.
- **Text and outlines:** deep navy / near-black navy.
- **Supporting fills and lines:** pale blue-gray or warm gray for quiet card fills, secondary connectors, shadows, and grouping regions.
- **Sketch style:** prefer white or near-background card interiors with thin deep navy outlines; avoid large colored fills.

### Dark mode

Use these colors by default for non-workflow documentation graphics:

- **Background:** transparent or `#161416` only. If using texture, keep the base background exactly `#161416` and add only subtle low-contrast patterning on top.
- **Primary accent:** `#BE123C` deep rose for active paths, arrows, highlights, emphasis strokes, selected nodes, and small icon fills.
- **Text and outlines:** off-white / very light cool gray.
- **Supporting fills and lines:** muted blue-gray or warm gray for quiet card fills, secondary connectors, shadows, and grouping regions.
- **Sketch style:** preserve the same thin-outline reference style in dark mode: use dark near-background card interiors, off-white line icons and outlines, muted secondary strokes, and small deep-rose highlights rather than heavy filled panels.

New docs graphics should use transparent, `#fcf9fa`, or `#161416` backgrounds as specified above.

## Background

Create documentation-friendly backgrounds, compatible with the Mintlify backgrounds.

Good background treatments:

- subtle paper grain or soft technical-notebook texture;
- pale blue-gray sketch shadows under main cards or nodes;
- tiny low-contrast connector dots or guide marks near margins;

Rules:

- Keep the center of the graphic clean enough for labels and connectors.
- Keep the border of the graphic the solid background color, to integrate seamlessly with the Mintliy background
- Keep patterns low contrast and secondary to the diagram.
- Do not place texture behind dense labels or code-like terms.
- Do not make the graphic look like a presentation slide.
- Do not include any logo or logo watermark.

## Tilebox workflow diagram palette

Only when the user explicitly asks for a Tilebox workflow DAG diagram, D2 workflow diagram, task-state DAG, retry DAG, optional-subtask tree, or runner execution DAG, use the workflow-specific D2 palette from `assets/workflows/diagrams/generate.py` instead of painter and instead of the default palette.

Reference source:

- `assets/workflows/diagrams/generate.py`

Light workflow theme:

- **Background:** `#FCF9FA`
- **Queued task:** fill `#FFF0F5`, stroke `#504448`, text `#000000`
- **Running task:** fill `#AFEEEE`, stroke `#0e5253`, text `#000000`
- **Computed task:** fill `#F0FFF0`, stroke `#3f4b40`, text `#000000`
- **Failed task:** fill `#FA8072`, stroke `#4a1511`, text `#000000`
- **Skipped task:** fill `#fcf3ae`, stroke `#877e3c`, text `#000000`
- **Subtask edge:** stroke `#170206`
- **Dependency edge:** dashed stroke `#9B1A47`
- **Diagram title:** text `#170206`

Dark workflow theme:

- **Background:** `#161416`
- **Queued task:** fill `#A37200`, stroke `#fcc76f`, text `#FFFFFF`
- **Running task:** fill `#3E7079`, stroke `#b1e5ef`, text `#FFFFFF`
- **Computed task:** fill `#265429`, stroke `#b7ebb8`, text `#FFFFFF`
- **Failed task:** fill `#A31800`, stroke `#f78d79`, text `#FFFFFF`
- **Skipped task:** fill `#c6b63c`, stroke `#ffed67`, text `#FFFFFF`
- **Subtask edge:** stroke `#F4F1F4`
- **Dependency edge:** dashed stroke `#F97F76`
- **Diagram title:** text `#F4F1F4`

Workflow D2 conventions:

- put source diagrams in `assets/workflows/diagrams/*.d2`;
- generate SVG outputs into `assets/workflows/diagrams/svg/`;
- run `python generate.py` from `assets/workflows/diagrams/` after editing workflow diagrams;
- commit both `.d2` source and generated `.svg` / `.dark.svg` outputs;
- use `Geist` font files through the existing generator;
- keep task labels short and use D2 classes such as `queued`, `running`, `computed`, `failed`, `skipped`, `optional`, `subtask-edge`, and `dependency-edge`.

Only use this workflow-specific palette for explicit Tilebox workflow DAG / D2 diagrams. For all other documentation graphics, use painter and the default documentation palette.

## Composition rules

Default to an aspect ratio that fits the page content:

- **Wide architecture or flow diagrams:** 16:9 PNG.
- **Tall trees or lifecycle diagrams:** portrait PNG.
- **Small inline concepts:** compact PNG with minimal padding.

Rules:

- Make the diagram understandable without surrounding prose, but do not duplicate the prose.
- Keep one primary idea per graphic.
- Put labels inside or adjacent to their objects.
- Use consistent connector direction and spacing.
- Prefer left-to-right flow for processes and top-to-bottom flow for trees.
- Use grouping boxes only when they reduce ambiguity.
- Leave enough padding for rendering in Mintlify cards and pages.
- Use decorative motifs only as subtle background texture or to clarify structure.

## Choosing the implementation format

Use this order:

1. **Painter-generated PNGs** for documentation graphics by default.
2. **D2 through `assets/workflows/diagrams/generate.py`** only when the user explicitly asks for a Tilebox workflow DAG / D2 diagram or updates an existing workflow DAG source.

Do not choose hand-authored SVGs or generic source-backed diagram tooling for new docs graphics. The desired default is painter-generated PNGs because they look better in the docs. The only built-in non-painter path in this skill is the explicit Tilebox workflow DAG / D2 exception. If a normal documentation diagram would benefit from iteration, iterate with painter prompts and saved PNG outputs instead of creating a source-backed SVG.

## Creating a new documentation graphic

1. Identify the page and asset folder. Use the nearest product folder under `assets/`.
2. Read nearby MDX pages and assets to match naming, embedding, and visual density.
3. Use painter immediately and produce PNGs. Only use D2 if the user explicitly asks for a Tilebox workflow DAG / D2 diagram.
4. Define the smallest diagram that explains the target concept.
5. Create both light and dark variants unless the user asks otherwise.
6. Add or update the MDX embedding only if the user asked to place the graphic in the docs.
7. Report the generated PNG paths and any caveat about text legibility or exact wording.

## Editing an existing documentation graphic

1. Use painter to edit existing PNG documentation graphics by default.
2. For explicit workflow DAG / D2 diagrams, find the `.d2` source first. Do not edit generated workflow SVG output if a D2 source file exists.
3. Preserve the existing naming and light/dark pairing.
4. Keep layout changes limited to what the user requested.
5. Verify both mode variants exist and are referenced correctly.

## Painter prompt patterns

Use painter as the default tool.

Generate one image per painter call. For paired light/dark outputs, first generate the light PNG, then use that image as the input for a dark-mode color-only edit.

### Light documentation graphic prompt base

> Create a clean technical Tilebox documentation graphic for docs.tilebox.com as a PNG, matching the best-practice technical sketch style from `references/best-practice-technical-sketch.jpeg`: thin dark outlines, mostly white or near-background cards, minimal black line-art icons with tiny deep-rose highlights, restrained red action arrows, generous whitespace, and a calm hand-sketched field-notes feel without looking childish. Use Geist typography, with Geist Mono for code-like labels and technical identifiers. Use a transparent background or exactly `#fcf9fa` as the base background, deep navy text and outlines, restrained deep rose accents exactly `#BE123C`, and pale blue-gray or warm-gray secondary lines. Prefer rounded rectangles for actors/systems/grouped lists and hexagons for loop steps or lifecycle states when useful. Add only tasteful low-contrast background motifs, such as subtle paper grain, faint honeycomb/technical guide marks near the margins, or soft sketch shadows, while keeping the center clean and readable and the edges the solid background color. Create a precise architecture / flow / relationship diagram with short, highly legible labels and limited simple iconography only where it clarifies the content. Do not include any Tilebox logo, logo watermark, slide title, conclusion text, section number, footer, or full-canvas background pattern. Avoid clutter, colored filled cards, gradients, glossy depth effects, decorative corporate vector art, overdone icons, cursive, childish style, tiny text, and low contrast.

### Dark documentation graphic prompt base

Use this only when creating a dark-mode-only graphic with no light source image:

> Create a clean technical Tilebox documentation graphic for docs.tilebox.com as a PNG, not a presentation slide, matching the best-practice technical sketch style from `references/best-practice-technical-sketch.jpeg` adapted to dark mode: thin off-white outlines, dark near-background cards, minimal light line-art icons with tiny deep-rose highlights, restrained red action arrows, generous whitespace, and a calm hand-sketched field-notes feel without looking childish. Use Geist typography, with Geist Mono for code-like labels and technical identifiers. Use a transparent background or exactly `#161416` as the base background, off-white text and outlines, restrained deep rose accents exactly `#BE123C`, and muted blue-gray or warm-gray secondary lines. Prefer rounded rectangles for actors/systems/grouped lists and hexagons for loop steps or lifecycle states when useful. Add only tasteful low-contrast background motifs, such as subtle paper grain, faint honeycomb/technical guide marks near the margins, or soft sketch shadows, while keeping the center clean and readable and the edges the solid background color. Create a precise architecture / flow / relationship diagram with short, highly legible labels and limited simple iconography only where it clarifies the content. Do not include any Tilebox logo, logo watermark, slide title, conclusion text, section number, footer, or full-canvas background pattern. Avoid clutter, colored filled cards, gradients, glossy depth effects, decorative corporate vector art, overdone icons, cursive, childish style, tiny text, and low contrast.

### Dark-from-light color-only edit prompt base

> Edit the provided light-mode Tilebox documentation graphic into dark mode. ONLY EDIT THE COLORS. DO NOT CHANGE ANY LAYOUT OR CONTENT. Preserve every label, icon, node, arrow, position, size, spacing, texture placement, and composition exactly. Change the base background to transparent or exactly `#161416`; change deep navy text and outlines to off-white / very light cool gray; keep the primary accent exactly `#BE123C`; adapt white or near-background cards to dark near-background cards; adapt pale blue-gray or warm-gray secondary lines, fills, shadows, and background texture to muted dark-mode equivalents. Preserve the thin technical sketch style, minimal line icons, and restrained red action accents. Do not add any Tilebox logo, logo watermark, slide title, conclusion text, section number, footer, or full-canvas background pattern. The dark mode graphic should be a 1-to-1 drop in replacement for the light version, users switching themes should just notice a color change, without any layout or other different jumps between the two versions.

### Edit prompt base

> Edit the provided Tilebox documentation graphic. Make only these changes: [specific changes]. Preserve the clean technical sketch documentation style from `references/best-practice-technical-sketch.jpeg`: thin outlines, mostly unfilled cards, minimal line icons, restrained deep-rose action accents, generous whitespace, Geist typography, Geist Mono for code-like labels where appropriate, no logos, no slide framing, no heavy or central background pattern, and all other content unchanged unless requested. Use the correct mode palette: [light or dark palette].

## Text handling

Generated text in images can drift. Keep text short and inspect the output carefully.

Prefer:

- short labels;
- entity names;
- state names;
- method or field names;
- small numeric markers;
- simple arrows and connectors.

Avoid:

- paragraphs inside diagrams;
- marketing claims;
- page headings inside images;
- tiny legends;
- repeated labels that can be represented by grouping or color.

## When to ask before proceeding

Ask a short clarification if:

- the target page or asset folder is unknown and there is no obvious location;
- the content of the diagram is underspecified;
- the user asks to overwrite existing image files and overwrite intent is unclear;
- exact aspect ratio or export format matters but was not specified.

Do not ask whether to make light and dark versions unless the user’s instruction conflicts with the default. The default is both.
