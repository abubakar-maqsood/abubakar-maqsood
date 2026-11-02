# GitHub profile installation — abubakar-maqsood

Your profile repo already exists: https://github.com/abubakar-maqsood/abubakar-maqsood

## Replace the current README and add the new assets

1. Extract the ZIP locally. **Do not upload the ZIP as a single file.**
2. Open your profile repository. Upload `README.md` and the contents of `assets/`, `data/`, `scripts/`, and `.github/workflows/` to the **repository root**, keeping their paths.
3. If files already exist, GitHub may prompt you to overwrite or replace files. You can also upload through GitHub Desktop/VS Code (more reliable for nested `.github` folders).
4. Commit with: `refactor: refresh animated profile and project dashboard`.
5. Open https://github.com/abubakar-maqsood and confirm the cover, illustrated laptop avatar, milestones and links render.

**Important:** This version replaces the large illustrated banner with a clean SVG header, and shows the transparent waving avatar only in the About section. Old `assets/hero-wave.gif` can be left in the repository (unused) or deleted later.

## Edit project progress accurately

- Open `data/projects.json`.
- Review the `done` state of *each* milestone and the project's `next` action. The file contains editable starter values, not independently verified completion.
- For local regeneration run `python scripts/render_dashboard.py` (uses the Python standard library only).
- If `.github/workflows/dashboard.yml` is present, pushing changes to the JSON or script triggers an automatic rebuild and commit.
- If GitHub Actions cannot push, verify **Settings → Actions → General → Workflow permissions** and grant write permission if permitted; the workflow itself asks only for `contents: write`.

## Optional contribution snake

- Upload `.github/workflows/snake.yml`.
- In your repository open **Actions → Generate contribution snake → Run workflow**.
- Wait for a successful run and check that the `output` branch contains `github-snake.svg` and `github-snake-dark.svg`.
- In `README.md`, remove the HTML comment markers around the optional Contribution trail section and commit.
- If activity is sparse, that is okay; the graph reflects published contributions. No mock activity is created.

## Profile sidebar details

Name: Muhammad Abubakar Maqsood

Bio (paste into Settings → Public profile):
`Software Developer | Frontend, Shopify & SEO | Applied AI & Research`

Website: https://ayhanpk.com/

LinkedIn: https://www.linkedin.com/in/abu-ba-kar/ (confirm that this is your current public URL)

Location: use your real current location, not an old city if you have moved.

Timezone: Pakistan Standard Time UTC+05:00, if you want the displayed clock to match Pakistan.

## Learning vs work experience

- WordPress and Elementor are deliberately **not listed**.
- Python, Firebase, MySQL, SQLite, Electron, React and ML appear in **Currently exploring**, not the professional toolset.
- Prompt engineering is listed as a familiar practice within AI-assisted development.
- Hackathons are described as participation/interest; no prizes, formal publications, or unverified credentials are claimed.
- Project status and milestones are editorial, user-maintained information.

## GitHub rendering limits

GitHub profile READMEs cannot run arbitrary JavaScript or a live application. The cover and tracker use SVG, and the illustrated greeting uses an animated GIF. Images can appear static for viewers who disable animation. The Github Actions workflow refreshes the tracker **when you edit checklists**; it cannot detect task completion automatically.
