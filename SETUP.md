# Installation: complete animated GitHub profile

This ZIP is for the **existing** profile repository:

https://github.com/abubakar-maqsood/abubakar-maqsood

## Final layout

1. Latest approved cream/charcoal/gold cover, with handwritten signature and end star, **Vibe Coding** and AI/ML research interest labels. The cover itself is a compressed, static WebP image.
2. Profile links: LinkedIn, website and repositories.
3. Small, centered, transparent Bitmoji behind a laptop (static).
4. Four research/graduate-study headlines that type, erase and repeat (animated GIF).
5. Research-first introduction with academic background and a careful description of learning goals.
6. Two equal, centered rows of technology icons; learning technologies clearly labeled.
7. Completed public/practice project cards (no made-up live demos).
8. Current projects and animated milestone bars, which grow from zero to manually recorded positions.
9. Graduate-study goals, current activities and collaboration.

## Replace in your current repository

1. Download and extract the ZIP on your computer.
2. In GitHub Desktop, clone/open `abubakar-maqsood/abubakar-maqsood`.
3. Copy the **contents** of the extracted folder (not the outer folder itself) into the repository root, replacing existing files.
4. Check that `README.md` and `assets/` are at the repository root and `.github/workflows/` is present.
5. Commit the update and click **Push origin**.
6. Open https://github.com/abubakar-maqsood and refresh.

The web uploader can have trouble replacing many existing files and hidden `.github` folders. GitHub Desktop is recommended. Do **not** upload the ZIP itself to GitHub.

## Customize project milestones

Edit `data/projects.json` to reflect actual milestone states. The bundled counts are starter checklists, **not verified project completion percentages**. For local regeneration:

```bash
python -m pip install 'Pillow>=10,<13'
python scripts/render_dashboard.py
```

The `.github/workflows/dashboard.yml` workflow can regenerate dashboard files after changes to the JSON, but GitHub Actions permissions and successful execution must be checked in your own repository.

## Files and loading

- `assets/top-cover-banner.webp`: latest approved cover, compressed for faster loading
- `assets/center-bitmoji.webp`: small static transparent avatar
- `assets/research-headlines-typing.gif`: looping text animation
- `assets/project-dashboard-grow.gif`: growing milestone bar animation
- `.github/workflows/`: dashboard update and optional snake workflows

The banner and avatar are intentionally static to keep the profile lightweight; the rotating headlines and project tracker are genuinely animated.
