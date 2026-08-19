# Publishing

Setup is complete. The pipeline is:

- **Push to `main`** (or run the *Render & Publish Book* workflow manually from the Actions tab) → GitHub Actions renders the book with Quarto and publishes `_book/` to the `gh-pages` branch.
- **GitHub Pages** serves the book at **https://anandpreshob.github.io/ai-medical-imaging-book/**.
- The personal website (www.anandpreshob.com) links out to that URL from its "Textbook" nav link and homepage card. The two repos are fully independent — there is no content sync between them.

## Local preview (optional)

Install [Quarto](https://quarto.org/docs/get-started/), then:

```bash
cd /Users/anandkadumberi/Projects/ai-medical-imaging-book
quarto preview
```
