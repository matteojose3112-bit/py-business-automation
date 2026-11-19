# Python Business Automation Toolkit

> Clean, inspect, and export business CSV data through a repeatable Python workflow.

**Status:** MVP implemented; deployment and runtime verification pending  
**Primary language:** Python 3  
**Framework:** Streamlit  
**Live demo:** Pending deployment  
**Deployment target:** Render

## Overview

Small teams often spend time cleaning spreadsheets, correcting inconsistent column names, removing duplicate records, and preparing data-quality summaries. This project provides a simple, repeatable workflow for those tasks.

Upload a CSV, choose the transformations, review the cleaned data and quality metrics, then download the processed dataset and a separate quality report.

## Features

- Upload CSV files through a browser interface.
- Normalize column names into consistent snake_case labels.
- Trim leading and trailing whitespace in text fields.
- Remove completely empty rows.
- Remove duplicate records.
- Review original and processed data previews.
- Inspect per-column missing-value and uniqueness metrics.
- Download the cleaned dataset and quality report as CSV files.
- Reuse the cleaning logic as an importable Python module.

## Technology

- Python 3
- Streamlit
- pandas
- pytest

## Project structure

```text
py-business-automation/
├── app.py
├── automation.py
├── requirements.txt
├── render.yaml
├── sample-data/
│   └── customers.csv
├── tests/
│   └── test_automation.py
├── .gitignore
├── README.md
├── ROADMAP.md
└── CHANGELOG.md
```

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and launch the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Run the automated tests:

```bash
pytest -q
```

## Try the sample data

Use the **Load sample dataset** option in the app, or upload [sample-data/customers.csv](sample-data/customers.csv). The included records are synthetic and contain no real customer information.

## Data handling and privacy

The demo processes uploaded data in the active application session and does not intentionally persist uploaded files. Do not upload confidential, sensitive, or personally identifiable customer information. Public demo hosting is not a substitute for a private, compliance-reviewed data-processing environment.

## Deployment

A Render configuration is included in `render.yaml`. Deployment is not yet confirmed. The live URL will be published here only after the service has successfully deployed and the application has been checked.

## Roadmap and release history

- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

## Portfolio capabilities demonstrated

Python scripting, pandas data processing, reusable function design, CSV workflows, data-quality reporting, Streamlit application development, and automated testing.

## Current limitations

- CSV input only; Excel support is planned.
- No persistent storage or user accounts.
- No background processing for very large files.
- Data-quality checks are descriptive and do not infer business-specific correctness.
- Deployment and automated test execution still need verification.
