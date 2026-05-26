# AGENTS.md

## Purpose

This repository contains the Mintlify source for [docs.tilebox.com](https://docs.tilebox.com). Use this file to keep documentation updates consistent with the current information architecture, writing style, and tooling.

## Required Writing Skill

Always read and respect the `writing-technical-content` skill before writing, drafting, revising, or outlining technical documentation, guides, or long-form content in this repository.

## Information Architecture

Navigation is defined in `docs.json` and currently follows this top-level structure:

1. `Documentation`: product docs, concepts, and capability docs for Datasets, Storage, and Workflows.
2. `User Guides`: task-focused walkthroughs (mostly step-by-step procedures).
3. `Languages & SDKs`: language-specific install and usage docs for Python and Go.
4. `API Reference`: method-level reference pages for Python and Go clients.
5. `Changelog`: product updates.

When adding or moving pages:

1. Keep `docs.json` in sync with actual files.
2. Keep pages grouped by product area (`datasets/`, `workflows/`, `storage/`, `sdks/`, `guides/`, `api-reference/`).
3. Preserve the current pattern where high-level landing pages link to deeper pages via `Card`/`HeroCard` blocks.

## Diátaxis Mapping

We follow [Diátaxis](https://diataxis.fr/). Pick one primary intent per page and keep it focused.

1. Tutorial: onboarding learning journeys (for example `quickstart.mdx`).
2. How-to guide: concrete goals via ordered steps (primarily under `guides/**`).
3. Explanation: conceptual understanding and mental models (for example `datasets/concepts/**`, `workflows/concepts/**`, introductions).
4. Reference: factual lookup docs (primarily `api-reference/**`, parameter tables, changelog entries).

Practical rule: if a page starts drifting into multiple intents, split it into separate pages and cross-link them.

## Writing Style And Tone

Follow the existing house style:

1. Audience: developers and technical users integrating Tilebox.
2. Voice: direct, clear, and pragmatic; prefer active voice and short paragraphs.
3. Person: usually second person (`you`) for guidance.
4. Tense: present tense for behavior and capabilities.
5. Scope: explain what the reader needs now; avoid broad marketing language.

Common page flow patterns in this repo:

1. Short context paragraph after frontmatter.
2. `Related documentation` card section when useful.
3. Step-by-step sections for procedures.
4. `Next steps` links/cards at the end.

## Terminology, Capitalization, And Naming

Use consistent product language:

1. `Tilebox` (capital T) everywhere.
2. Product/module names: `Tilebox Console`, `Tilebox Datasets`, `Tilebox Workflows`.
3. Generic references are lowercase: `datasets`, `workflows`, `client`, `collection`, `job`, `task`.
4. Dataset kind names used in docs: `Timeseries` and `Spatio-temporal`.
5. Keep acronyms uppercase (`API`, `SDK`, `MCP`, `UUID`, `UTC`).

Heading style in the existing docs is mostly concise sentence-style phrases (with selective title casing). Match nearby pages rather than enforcing a new global style.

## MDX And Mintlify Conventions

For new non-reference pages, include frontmatter fields matching existing docs:

1. `title`
2. `description`
3. `icon`
4. Optional short `sidebarTitle` if the title is too long.

Prefer existing Mintlify components and patterns:

1. `CodeGroup` for multi-language examples (usually Python first, Go second when both exist).
2. `Steps`/`Step` for procedural flows.
3. `Tip`/`Note`/`Info`/`Warning` for callouts.
4. `Columns` + `Card` for internal navigation.
5. `Frame` for screenshots.

Images should follow the existing light/dark pattern when both variants exist:

```mdx
<img src="/path/light.png" className="dark:hidden" />
<img src="/path/dark.png" className="hidden dark:block" />
```

## Dev Tooling

Core tooling used in this repo:

1. Mintlify CLI for local preview and link checks.
2. Vale for prose linting.
3. `pre-commit` hook running Vale.
4. GitHub Actions CI for Vale + broken link checks.

Local setup and validation commands:

```bash
# install tooling
npm i -g mintlify
vale sync
pre-commit install

# run docs locally
mintlify dev

# lint prose
vale .

# check broken links
mintlify broken-links

# optional: run all hooks
pre-commit run --all-files
```

CI notes:

1. CI installs Node `24`.
2. CI installs `mdx2vast` before running Vale.
3. CI runs `vale sync && vale .` and `mintlify broken-links`.

## Diagrams And Assets

Workflow diagrams under `assets/workflows/diagrams/` are generated from `.d2` files via `generate.py`.

When updating workflow diagrams:

1. Edit the `.d2` source.
2. Regenerate SVG assets with `python generate.py` from `assets/workflows/diagrams/`.
3. Commit both source and generated SVG outputs.

## Update Checklist For Agents

For any substantial docs update, verify all of the following:

1. Page intent matches a single Diátaxis category.
2. Page is linked in `docs.json` in the correct section.
3. Internal links resolve and `mintlify broken-links` passes.
4. Vale warnings/errors are addressed or intentionally accepted.
5. New screenshots/assets are optimized and use correct paths.
6. Language and terminology match surrounding Tilebox docs.

## Notes On API Reference Pages

`api-reference/**` pages are reference-first and should remain concise and factual. Keep examples minimal and parameter descriptions explicit. Avoid turning reference pages into long tutorials; link to guides instead.
