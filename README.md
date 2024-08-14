# Tilebox Documentation

Welcome to the Tilebox documentation. It hosts the source code for the documentation deployed at [docs.tilebox.com](https://docs.tilebox.com).

This repository is built using [Mintlify](https://www.mintlify.com).

## Setting up your local environment

1. Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally.

```
npm i -g mintlify
```

2. Install [vale](https://vale.sh/docs/vale-cli/installation/)

And then run the following command once to sync the vale styles

```
vale sync
```

3. Set up pre-commit hooks

```
pre-commit install
```

## Previewing changes

Run the following command at the root of your documentation (where mint.json is)

```
mintlify dev
```

## Checking for issues

To run the vale linter locally, and check for issues, run the following command

```
vale .
```

Checking for broken links

```
mintlify broken-links
```
