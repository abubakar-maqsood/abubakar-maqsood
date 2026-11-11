# Abubakar GitHub Profile — Complete Animated Edition

This package includes the updated GitHub README, all required custom SVG cards, the rotating titles, and the **fixed animated waving developer GIF**. The extra hand has been removed.

## Installation

1. Open your GitHub profile repo: https://github.com/abubakar-maqsood/abubakar-maqsood
2. Back up your existing README and any custom assets that you want to keep.
3. Replace the root `README.md` with the file from this package.
4. Upload the entire `assets/2026-refresh/` folder, including `center-bitmoji-wave.gif`.
5. Upload `scripts/generate_activity.py` and `.github/workflows/profile-activity.yml` into their exact folders.
6. Commit all changes. GitHub will display the fixed waving GIF immediately.

## Activity workflow

The activity chart and snake are included as styled previews. To replace those previews with real public activity data and a generated contribution snake:

- Go to **Actions > Update profile activity and snake > Run workflow**.
- GitHub Actions must be enabled and have **Read and write permissions** for `GITHUB_TOKEN` if your repository settings restrict them.
- The action updates the chart/snake images daily. The generated snake replaces the custom preview design.
- The streak statistics image uses an external provider.

The GIF itself does not require GitHub Actions. It is animated and plays from a local file in your profile repository.

## Contents

- `README.md`: full profile
- `assets/2026-refresh/center-bitmoji-wave.gif`: edited and animated waving developer
- `assets/2026-refresh/roles-typewriter.gif`: role animations
- `assets/2026-refresh/hero-header.svg`: GitHub header
- `assets/2026-refresh/card-*.svg`: recent project cards
- `assets/2026-refresh/activity-wave.svg`, `activity-events.svg`: activity display
- `assets/2026-refresh/github-snake.svg`, `github-snake-dark.svg`: snake previews
- `.github/workflows/profile-activity.yml`: GitHub Actions workflow
- `scripts/generate_activity.py`: public event chart updater
