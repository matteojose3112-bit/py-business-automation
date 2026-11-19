# Changelog

All notable changes to this project are documented here.

## [0.1.0] — 2026-11-19

### Added
- Streamlit interface for uploading and previewing CSV files.
- Reusable CSV cleaning pipeline in `automation.py`.
- Optional whitespace trimming and snake_case header normalization.
- Optional removal of completely empty rows and duplicate records.
- Per-column data-quality report with missing and unique-value metrics.
- CSV downloads for cleaned data and the quality report.
- Synthetic customer dataset for demonstration.
- Initial pytest coverage for transformations and reporting.
- GitHub Actions workflow to run pytest on pushes and pull requests.
- Render service configuration and public Free-plan deployment.

### Changed
- README now links to the live application and documents local setup, privacy notes, and known limitations.
- Roadmap updated to record successful deployment and retain outstanding verification tasks.

### Deployment
- Live application: https://python-business-automation.onrender.com
- Render confirmed the build and deployment succeeded.
- Application logs confirm Streamlit started and the service was marked live.

### Verification still pending
- Automated test suite execution has not yet been confirmed.
- End-to-end browser checks of sample loading, cleaning, previews, and downloads remain pending.
