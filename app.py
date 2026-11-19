"""Streamlit interface for the Business Automation Toolkit."""
from __future__ import annotations

from io import BytesIO

import pandas as pd
import streamlit as st

from automation import clean_dataframe, quality_report

st.set_page_config(page_title="Business Automation Toolkit", page_icon="⚙️", layout="wide")

st.title("Business Automation Toolkit")
st.caption("Clean, validate, and prepare business CSV data in a repeatable workflow.")
st.markdown(
    "A practical data-preparation utility for operations teams and small businesses. "
    "Upload a CSV, choose the transformations, inspect the results, and export clean files."
)

with st.sidebar:
    st.header("Cleaning options")
    trim = st.checkbox("Trim text whitespace", value=True)
    normalize = st.checkbox("Normalize column names", value=True)
    remove_empty = st.checkbox("Remove completely empty rows", value=True)
    remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
    st.divider()
    st.caption("Files are processed in this session. Do not upload confidential or sensitive data.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"], help="UTF-8 CSV files are recommended.")

if uploaded is None:
    st.info("Upload a CSV file to begin. You can also try the included synthetic sample.")
    if st.button("Load sample dataset"):
        st.session_state["sample_mode"] = True
    if st.session_state.get("sample_mode"):
        source = pd.DataFrame({
            "Customer Name": ["  Ana Ruiz ", "Luis Gómez", "Ana Ruiz", None, "Marta Díaz"],
            "Email Address": ["ana@example.com", "luis@example.com", "ana@example.com", None, "marta@example.com"],
            "Region": [" Quindio ", "Bogota", " Quindio ", None, "Pereira"],
            "Revenue": [120000, 95000, 120000, None, 180000],
        })
    else:
        st.stop()
else:
    try:
        source = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"We couldn't read this CSV file: {exc}")
        st.stop()

try:
    cleaned, summary = clean_dataframe(
        source,
        trim_whitespace=trim,
        normalize_column_names=normalize,
        remove_empty_rows=remove_empty,
        remove_duplicates=remove_duplicates,
    )
except Exception as exc:
    st.error(f"Cleaning failed: {exc}")
    st.stop()

st.subheader("Processing summary")
metrics = st.columns(4)
metrics[0].metric("Original rows", summary.original_rows)
metrics[1].metric("Processed rows", summary.processed_rows)
metrics[2].metric("Empty rows removed", summary.removed_empty_rows)
metrics[3].metric("Duplicates removed", summary.removed_duplicate_rows)

left, right = st.columns(2)
with left:
    st.markdown("#### Input preview")
    st.dataframe(source.head(100), use_container_width=True)
with right:
    st.markdown("#### Cleaned preview")
    st.dataframe(cleaned.head(100), use_container_width=True)

st.subheader("Data quality report")
report = quality_report(cleaned)
st.dataframe(report, use_container_width=True, hide_index=True)

csv_bytes = cleaned.to_csv(index=False).encode("utf-8-sig")
report_bytes = report.to_csv(index=False).encode("utf-8-sig")
st.subheader("Export")
col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download cleaned CSV",
        data=csv_bytes,
        file_name="cleaned_business_data.csv",
        mime="text/csv",
        use_container_width=True,
    )
with col2:
    st.download_button(
        "Download quality report",
        data=report_bytes,
        file_name="data_quality_report.csv",
        mime="text/csv",
        use_container_width=True,
    )

with st.expander("How this tool handles your data"):
    st.write(
        "The app processes the uploaded file in memory for the active session. "
        "It does not intentionally persist uploaded files. Avoid uploading personal, "
        "financial, health, or confidential customer information to this public demo."
    )
    st.json(summary.to_dict())
