# GitHub profile: full animated version

**Repository:** `abubakar-maqsood/abubakar-maqsood` (public)

## Replace your existing files

1. Extract the ZIP to your computer. **Do not upload the ZIP itself.**
2. Open your existing profile repository on GitHub.
3. Upload the contents of this extracted folder **at repository root**, preserving `README.md`, `assets/`, `data/`, `scripts/`, and `.github/workflows/`.
4. Use GitHub Desktop (recommended): clone the existing repository, copy the extracted files into the cloned folder and confirm replacement, then Commit to main and Push origin. This includes the hidden `.github` folder.
5. Commit with `Refresh animated GitHub profile` and reload `https://github.com/abubakar-maqsood`.

**IMPORTANT:** GitHub's web uploader is not a reliable bulk-replacement tool for files that already exist. GitHub Desktop is recommended. Do not delete your repository or create a new one. Preserve the exact paths. Old, unused assets such as `assets/hero-wave.gif` can be deleted later, but are harmless if left in place.

## Animations included

- `assets/name-cover-typing.gif`: real animated typing of your full name. No character in the cover.
- `assets/about-avatar-wave.gif`: the **exact uploaded illustrated character** with a gently waving raised hand and laptop in front; the face, suit, and laptop are stationary.
- `assets/about-avatar-transparent.png`: the original source image used to make that animation.
- `assets/project-dashboard-grow.gif`: each milestone bar starts at zero and fills to the checklist fraction; it loops.
- `assets/footer-line.svg`: subtle footer pulse (browser SVG support varies).
- `assets/project-dashboard.svg`: SVG alternative with animated width change where SVG animation is supported.
- `assets/name-cover-still.png` and `assets/project-dashboard-still.png`: static poster frames.

All main animations are GIFs for consistent display in GitHub's README. Markdown doesn't allow custom JavaScript. GIFs loop whenever they are viewed; they don't update milestone data by themselves.

## Updating project progress

Edit `data/projects.json`. Set milestone `done` to `true` only after it is actually complete, and update `phase` and `next` as necessary. **Do not treat demo milestones as verified without checking**. The tracker reports your manually edited milestones, not actual percent of code or task completion.

When GitHub Actions workflow `Refresh animated project tracker` is enabled, it runs after a commit to `data/projects.json`, regenerates `assets/project-dashboard-grow.gif`, `assets/project-dashboard.svg` and poster, then commits updated assets. The workflow also generates `assets/name-cover-typing.gif` (with the same name).

Run locally (Python 3.10+):

```bash
python -m pip install Pillow
python scripts/render_animations.py
```

**If the Action fails to push:** Repository Settings > Actions > General > Workflow permissions > Read and write permissions, where your repository policy allows it. Then run the workflow manually in the Actions tab.

## Optional contribution snake

Run the `Generate contribution snake` workflow once in Actions. After verifying the `output` branch contains the SVG images, remove the `<!-- ... -->` comment around the optional contribution-snake section in `README.md` and commit. The snake reflects genuine GitHub contribution history, not project milestones. This step is optional.

## Appearance and accessibility

Animated GIFs may not respect system Reduced Motion preferences. Prefer the two `*-still.png` alternatives in the README if you want to disable motion. The design intentionally keeps animations restrained, with legible contrast and no moving background behind About Me text.

## Regenerate the exact Bitmoji hand-wave (optional)

The included GIF is already finished; **you do not have to run this step**. To remake it using the supplied original illustration:

```bash
python -m pip install Pillow numpy opencv-python
python scripts/render_avatar_wave.py
```

This affects only the Bitmoji GIF. The project progress workflow does not alter your avatar.
