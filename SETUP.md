# One-time setup (do these once, ~10 minutes)

The repo is ready on your machine and git-initialized. What remains needs your GitHub login, so it's on you:

## 1. Create the GitHub repo and push

```bash
cd /Users/anandkadumberi/Projects/ai-medical-imaging-book
gh repo create anandpreshob/ai-medical-imaging-book --public --source=. --push
# or create it in the GitHub UI, then:
# git remote add origin https://github.com/anandpreshob/ai-medical-imaging-book.git
# git push -u origin main
```

## 2. Enable GitHub Pages

After the first Action run creates the `gh-pages` branch:
Repo → **Settings → Pages** → Source: *Deploy from a branch* → Branch: `gh-pages` / `/ (root)` → Save.

Book appears at **https://anandpreshob.github.io/ai-medical-imaging-book/**.

## 3. Add the website-sync token

The Action pushes the rendered book into `personal-website/book/`, which triggers your existing Firebase deploy.

1. GitHub → your avatar → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**
2. Name: `book-website-sync` · Repository access: **Only select repositories → `anandpreshob/personal-website`** · Permissions: **Contents → Read and write**
3. Copy the token, then in the **ai-medical-imaging-book** repo: **Settings → Secrets and variables → Actions → New repository secret** → Name: `WEBSITE_SYNC_TOKEN`, Value: the token.

Until the secret is set, the Action still publishes to GitHub Pages and simply skips the website sync (no failure).

## 4. First render

Push anything to `main` (or run the workflow manually from the Actions tab). After it finishes:
- GitHub Pages mirror is live
- `personal-website` gets a commit adding `book/` → Firebase auto-deploys → **www.anandpreshob.com/book/** is live

## Local preview (optional)

Install [Quarto](https://quarto.org/docs/get-started/), then:

```bash
cd /Users/anandkadumberi/Projects/ai-medical-imaging-book
quarto preview
```

## Note on the website nav

The "Textbook" nav link and homepage card added to your website point to `/book/`, which 404s until step 4 completes. Deploy the book before (or together with) the website changes.
