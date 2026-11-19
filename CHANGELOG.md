# Changelog

All notable changes to this project are documented here.

## [Unreleased]

### Added
- Streamlit interface for uploading and previewing CSV files.
- Reusable CSV cleaning pipeline in `automation.py`.
- Optional whitespace trimming and snake_case header normalization.
- Optional removal of completely empty rows and duplicate records.
- Per-column data-quality report with missing and unique-value metrics.
- CSV downloads for cleaned data and the quality report.
- Synthetic customer dataset for demonstration.
- Initial pytest coverage for transformations and reporting.
- Render service configuration.

### Changed
- README now documents the implemented MVP, local setup, privacy notes, and current limitations.
- Roadmap updated to distinguish implemented work from pending verification and deployment.

### Pending verification
- Automated tests have been added but have not yet been executed in a verified environment.
- Render deployment and public URL have not yet been confirmed.
