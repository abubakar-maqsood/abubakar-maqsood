# Complete animated GitHub profile — Installation

Target repository: `abubakar-maqsood/abubakar-maqsood` (existing profile repo; do not create a new repo).

## Included behavior

- **Animated cover** (`assets/animated-cover.webp`): existing cream/charcoal/gold academic-desk design; small pencil draws the handwritten signature; name types/reveals; Information Technology appears below; lower fabric waves move subtly. All rendered inside one animated WebP, not an interactive site.
- **Centered Bitmoji** (`assets/center-bitmoji-wave.gif`): waves beside the laptop.
- **Rotating lines** (`assets/research-headlines-typing.gif`): research and study goals type, erase, repeat, on a transparent-looking clean background.
- **Research-first About Me**, two rows of tools (Python listed first), completed public projects, current prototypes.
- **Project milestones** (`assets/project-dashboard-grow.gif`): bars grow to manually entered checklist values. Not a GitHub activity counter or automatically verified progress.

## Replace files in the same repository

1. Download and extract ZIP on your computer.
2. Open your existing `abubakar-maqsood/abubakar-maqsood` repository in GitHub Desktop.
3. Copy the **contents** of this ZIP into the repository root and replace matching files (especially README.md, assets/, data/, scripts/, .github/).
4. Commit and **Push origin**.
5. Refresh https://github.com/abubakar-maqsood (Ctrl+F5 if browser caching delays images).

The GitHub web upload can be awkward for overwriting and hidden `.github` folders. GitHub Desktop recommended.

## Edit tracker

Update `data/projects.json`, then run `python scripts/render_dashboard.py` (requires Pillow) or enable `.github/workflows/dashboard.yml` after reviewing permissions. The existing milestone values are starter checklists and should be reviewed before claiming progress.

## Performance

The banner uses animated WebP to reduce size versus a full-size GIF. The rest of README stays simple Markdown plus image assets. Animation is subtle; banner text is kept static after it appears.
