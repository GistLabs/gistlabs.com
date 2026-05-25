# GistLabs Website

Jekyll site built with [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/), deployed to GitHub Pages via GitHub Actions.

## Local development

```sh
make serve
```

Visit http://localhost:4000 — the browser reloads automatically on file saves.

> **First time on macOS:** If `make install` fails with a compiler error, accept the Xcode license first:
> ```sh
> sudo xcodebuild -license accept
> ```

Other targets:

```sh
make build    # build the site to _site/
make clean    # remove the _site/ cache
```

## Content

- **Home page:** [index.markdown](index.markdown) — edit the YAML front matter to update the hero text, services, or CTA button
- **Blog posts:** [_posts/](_posts/) — add a new file named `YYYY-MM-DD-slug.markdown` with:
  ```yaml
  ---
  layout: single
  title: "Post Title"
  date: 2026-01-01
  categories: posts
  author: John Heintz
  ---
  ```
- **Navigation:** [_data/navigation.yml](_data/navigation.yml)
- **Site settings:** [_config.yml](_config.yml) — title, author, analytics ID, etc.
- **Custom styles:** [assets/css/main.scss](assets/css/main.scss)

## Deployment

Pushing to `main` triggers [.github/workflows/publish.yml](.github/workflows/publish.yml), which builds and deploys to GitHub Pages automatically.
