# AI in Medical Imaging: From Pixels to Practice

An open, evolving textbook on AI in medical imaging — written for clinicians, ML engineers, and AI agents at the same time. Human readers get dual-track explanations; agents get a fixed chapter structure, machine-readable CSV fact tables in [`data/`](data/), plain-markdown source, and an `llms.txt`.

**Read it:** https://anandpreshob.github.io/ai-medical-imaging-book/

## Current edition

All 22 chapters and five appendices have complete first drafts. Chapters 12–22 include 38 reproducible original SVG diagrams with captions and alt text. See [figure provenance](figures/remaining-chapters-provenance.md) and [catalog scope](data/README.md).

```bash
# Rebuild the diagrams for chapters 12–22
python scripts/remaining_figures.py
```

## How it's built

A [Quarto](https://quarto.org) book. Every push to `main` renders the book and publishes it to GitHub Pages automatically (see `.github/workflows/publish.yml`).

```bash
# Local preview
quarto preview
```

## Contributing

The dataset directories, model zoos, and FDA-cleared product indexes are **living tables** generated from the CSVs in [`data/`](data/). Spotted something missing or out of date? PRs that edit a CSV row are the easiest way to contribute.

## License

Text: CC BY-NC-SA 4.0 (proposed) · Code samples: Apache-2.0
