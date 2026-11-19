import pandas as pd

from automation import clean_dataframe, normalize_headers, quality_report


def test_normalize_headers_handles_spaces_duplicates_and_empty_names():
    assert normalize_headers(["Customer Name", "Customer Name", "!!!"]) == [
        "customer_name", "customer_name_2", "column_3"
    ]


def test_clean_dataframe_trims_drops_empty_and_duplicate_rows():
    source = pd.DataFrame({
        "Customer Name": [" Ana ", "Ana", None, "Luis"],
        "Email": ["ana@example.com", "ana@example.com", None, "luis@example.com"],
    })
    cleaned, summary = clean_dataframe(source)

    assert list(cleaned.columns) == ["customer_name", "email"]
    assert len(cleaned) == 2
    assert cleaned.iloc[0]["customer_name"] == "Ana"
    assert summary.original_rows == 4
    assert summary.processed_rows == 2
    assert summary.removed_empty_rows == 1
    assert summary.removed_duplicate_rows == 1


def test_quality_report_counts_missing_and_unique_values():
    frame = pd.DataFrame({"region": ["North", "South", None]})
    report = quality_report(frame)

    assert report.loc[0, "missing_values"] == 1
    assert report.loc[0, "unique_values"] == 2
    assert report.loc[0, "missing_percent"] == 33.33


def test_can_disable_transformations():
    source = pd.DataFrame({"Customer Name": [" Ana ", " Ana "]})
    cleaned, summary = clean_dataframe(
        source,
        trim_whitespace=False,
        normalize_column_names=False,
        remove_empty_rows=False,
        remove_duplicates=False,
    )

    assert list(cleaned.columns) == ["Customer Name"]
    assert len(cleaned) == 2
    assert summary.removed_duplicate_rows == 0
