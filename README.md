# AI in Medical Imaging: From Pixels to Practice

An open, in-progress textbook on AI in medical imaging — written for clinicians, ML engineers, and AI agents at the same time. Human readers get dual-track explanations; agents get a fixed chapter structure, machine-readable CSV fact tables in [`data/`](data/), plain-markdown source, and an `llms.txt`.

**Read it:** https://anandpreshob.github.io/ai-medical-imaging-book/

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
