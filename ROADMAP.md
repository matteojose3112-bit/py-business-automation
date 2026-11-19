# Roadmap

This roadmap tracks planned work. A task is complete only when implemented and verified.

## Phase 1 — Working foundation

- [x] Establish the Python project structure and dependencies.
- [x] Implement reusable CSV cleaning functions.
- [x] Add configurable header normalization and whitespace trimming.
- [x] Add empty-row and duplicate-row removal.
- [x] Add per-column data-quality reporting.
- [x] Add a Streamlit interface with previews and CSV exports.
- [x] Add synthetic sample data.
- [x] Add an initial automated test suite.
- [ ] Execute the test suite and resolve any failures.
- [ ] Verify local setup from a clean environment.

## Phase 2 — Core capabilities

- [ ] Add Excel import and export support.
- [ ] Add configurable column mapping and data validation rules.
- [ ] Add batch processing for multiple files.
- [ ] Add downloadable processing summaries and error logs.
- [ ] Expand tests for malformed files, unusual encodings, and edge cases.

## Phase 3 — Public demonstration

- [x] Add initial Render deployment configuration.
- [ ] Deploy the application to Render.
- [ ] Verify upload, cleaning, previews, and downloads on the live service.
- [ ] Add the verified public URL to the README.
- [ ] Add screenshots and a short usage walkthrough.

## Phase 4 — Quality and expansion

- [ ] Add file-size and row-count safeguards.
- [ ] Improve accessibility and responsive behavior.
- [ ] Add structured application logging and clearer user-facing errors.
- [ ] Review security and privacy considerations for public use.
- [ ] Tag a first stable release after acceptance checks pass.

## Definition of done

- A new user can run the project using documented instructions.
- Core transformations are covered by passing automated tests.
- Sample data is synthetic and reproducible.
- The deployed application is accessible and its core workflow has been verified.
- No credentials or private customer data are committed.
- Documentation accurately reflects the implemented features and known limitations.
