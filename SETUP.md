# Installation: GitHub profile for `abubakar-maqsood`

This is a GitHub **profile README**, not a website or a separate portfolio application. GitHub shows the root `README.md` from a public repository named **exactly the same as your username**.

## Step 1 — Create or open the matching repository

1. Log in as `abubakar-maqsood`.
2. Visit <https://github.com/new>.
3. Create a **Public** repository named **`abubakar-maqsood`**, OR open <https://github.com/abubakar-maqsood/abubakar-maqsood> if it already exists.
4. If you're creating it, leave **Add a README file** unchecked: this package already contains one.

## Step 2 — Upload the extracted files

**Extract the ZIP first.** Keep folders intact, and upload the contents to the repository root:

```text
README.md
assets/hero-wave.gif
assets/hero-preview.png
assets/typing.svg
assets/project-progress.svg
assets/footer.svg
data/projects.json
scripts/render_progress.py
.github/workflows/progress.yml
.github/workflows/snake.yml
PROFILE-SETTINGS.md
SETUP.md
PROJECT-README-TEMPLATE.md
.gitignore
```

The GitHub website uploader may not preserve hidden folders consistently. If `.github/workflows` is missing, add those workflow files through Git or create the paths directly on GitHub.

### Reliable Git CLI method

In a terminal, create the repository first on GitHub, then:

```bash
git clone https://github.com/abubakar-maqsood/abubakar-maqsood.git
cd abubakar-maqsood
# Copy the EXTRACTED contents of this package into this folder.
git add .
git commit -m "Add animated professional profile"
git push origin main
```

If a README already exists in that repository, replace or merge it instead of adding a second README.

## Step 3 — Check your profile

Open <https://github.com/abubakar-maqsood>. You should see the animated portrait/name, rotating tagline, skills, project summaries and an SVG progress tracker immediately. None of those initial visuals need GitHub Actions.

## Step 4 — Edit real project milestones

`data/projects.json` contains **starter checkboxes** informed by your described work, not verified production checklists. **Review every item before publishing.** Only mark a milestone `"done": true` when completed.

Regenerate locally (Python 3.9+, no packages required):

```bash
python scripts/render_progress.py
```

On GitHub, the `Render project milestones` workflow can refresh the SVG when `data/projects.json` is committed to `main`. If it can't push, check **Settings → Actions → General → Workflow permissions** and enable read/write for GitHub Actions if your policies permit it. You can also generate and commit the image locally, with no Actions at all.

## Step 5 — Optional contribution snake

1. Go to your profile repository → **Actions → Generate contribution snake → Run workflow**.
2. Wait for a successful run and confirm an **output** branch containing `github-snake.svg` and `github-snake-dark.svg`.
3. In `README.md`, remove the two HTML comment markers surrounding **OPTIONAL SNAKE SECTION** (not the content in between).
4. Commit. The snake updates on a daily schedule via GitHub Actions.

**Keep this section commented until the first successful workflow run** so visitors don't see broken images.

## Step 6 — Update your public settings

Open <https://github.com/settings/profile> and follow `PROFILE-SETTINGS.md`. Check especially the incorrect GMT−12 timezone in the screenshot; Pakistan is UTC+05:00.

## Step 7 — Pin useful repositories

Pin only repositories that actually exist and are understandable to a stranger. For each flagship project: `README`, clear problem, screenshots, tech stack, setup, sample output, limitations and attribution. A private or not-yet-published idea can stay in the profile's featured-work table without a dead GitHub URL.

## Technical limitations

GitHub README content does **not** support arbitrary JavaScript or actual interactive UI. Your portrait is a looping GIF; the name reveal and greeting accents animate. The milestone bars are SVG animations from a local JSON checklist and don't automatically know your coding progress. The contribution snake needs the optional workflow. External badges/skill icons can temporarily fail if their hosting services are unavailable.

**Accessibility:** the banner and SVGs have informative alt text. Some motion can be repetitive; keep your original profile photo visible as a static alternative and avoid flashing effects.
