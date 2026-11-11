# Install: fully patched GitHub profile (Nov 2026)

## What this corrects

1. **Broken activity graph:** Removed external `github-readme-activity-graph.vercel.app`. The README loads `assets/2026-refresh/activity-events.svg`, included in the ZIP. The workflow fills it with the last 30 days of **public GitHub events**. This is not a GitHub contribution count, and the API covers up to 100 recent public events.
2. **Broken snake:** Both snake SVGs exist locally in the ZIP before any automation runs. They initially show a tasteful activation placeholder. The workflow replaces them with the real contribution snake on the main branch.
3. **Duplicated projects:** Removed the project table, leaving four distinct illustrated cards with a concise status disclosure.

## Upload steps (important)

1. Open https://github.com/abubakar-maqsood/abubakar-maqsood and back up your existing README.
2. Upload / replace **README.md**, **assets/2026-refresh/**, **scripts/generate_activity.py**, and **.github/workflows/profile-activity.yml**. Preserve original `assets/animated-cover.webp`, `assets/center-bitmoji-wave.gif` and `assets/footer-line.svg`: the README still uses these original animations.
3. **Remove the old `.github/workflows/snake.yml`** if it exists. The new workflow handles both images and avoids conflicting snake output mechanisms.
4. Commit the files to your default branch (`main`). For hidden `.github` folder, using Git locally is simplest, or GitHub's Add file > Create new file with exact path `.github/workflows/profile-activity.yml`.
5. In repository Settings > Actions > General > Workflow permissions, select **Read and write permissions** (if the setting is available), then Save. GitHub Actions must be enabled.
6. On the repository's **Actions** tab, select **Update profile activity and snake**, click **Run workflow**, choose `main`, and run it.
7. Once the action passes and commits generated SVGs to `main`, the activity diagram and snake will show live data and update daily. GitHub's image caching might delay the refreshed display.

### Important behavior

- The initial graphics render without any workflow or third-party chart server. Their captions clearly indicate that synchronization hasn't happened yet.
- The streak statistic still uses `streak-stats.demolab.com`, a third-party service. If it goes down, remove just that single README `<img>`; the local graphs and snake are unaffected.
- GitHub cannot run arbitrary JavaScript in README files. These are GitHub-compatible SVG/GIF animations.
- Real public events are **not** equivalent to total contributions. Private contributions and some older events may not show. Snake comes from actual contribution data.
- The automation requires GitHub Actions permissions; uploading files by itself will not create real activity data.
- None of your older repositories are deleted. Their feature cards are intentionally removed.
