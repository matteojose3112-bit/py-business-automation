"""Reusable, testable CSV cleaning utilities for small-business workflows."""
from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Any

import pandas as pd


@dataclass
class CleaningSummary:
    original_rows: int
    processed_rows: int
    removed_empty_rows: int
    removed_duplicate_rows: int
    columns: int

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


def normalize_headers(columns: list[Any]) -> list[str]:
    """Convert column labels to stable snake_case identifiers."""
    normalized: list[str] = []
    seen: dict[str, int] = {}
    for index, value in enumerate(columns, start=1):
        label = str(value).strip().lower()
        label = re.sub(r"[^a-z0-9]+", "_", label).strip("_")
        label = label or f"column_{index}"
        count = seen.get(label, 0) + 1
        seen[label] = count
        normalized.append(label if count == 1 else f"{label}_{count}")
    return normalized


def clean_dataframe(
    frame: pd.DataFrame,
    *,
    trim_whitespace: bool = True,
    normalize_column_names: bool = True,
    remove_empty_rows: bool = True,
    remove_duplicates: bool = True,
) -> tuple[pd.DataFrame, CleaningSummary]:
    """Return a cleaned copy and a summary of the transformations."""
    result = frame.copy()
    original_rows = len(result)

    if normalize_column_names:
        result.columns = normalize_headers(list(result.columns))

    if trim_whitespace:
        for column in result.select_dtypes(include=["object", "string"]).columns:
            result[column] = result[column].map(
                lambda value: value.strip() if isinstance(value, str) else value
            )

    removed_empty = 0
    if remove_empty_rows:
        before = len(result)
        result = result.dropna(how="all")
        # Treat whitespace-only cells as empty after trimming.
        object_columns = result.select_dtypes(include=["object", "string"]).columns
        if len(object_columns):
            blank_mask = result[object_columns].apply(
                lambda col: col.map(lambda value: isinstance(value, str) and value == "")
            )
            result = result.loc[~blank_mask.all(axis=1)] if len(object_columns) == len(result.columns) else result
        removed_empty = original_rows - len(result)

    removed_duplicates = 0
    if remove_duplicates:
        before = len(result)
        result = result.drop_duplicates()
        removed_duplicates = before - len(result)

    summary = CleaningSummary(
        original_rows=original_rows,
        processed_rows=len(result),
        removed_empty_rows=removed_empty,
        removed_duplicate_rows=removed_duplicates,
        columns=len(result.columns),
    )
    return result.reset_index(drop=True), summary


def quality_report(frame: pd.DataFrame) -> pd.DataFrame:
    """Return one row per column with missing-value and uniqueness metrics."""
    total = len(frame)
    rows = []
    for column in frame.columns:
        series = frame[column]
        missing = int(series.isna().sum())
        rows.append({
            "column": str(column),
            "data_type": str(series.dtype),
            "missing_values": missing,
            "missing_percent": round((missing / total * 100) if total else 0.0, 2),
            "unique_values": int(series.nunique(dropna=True)),
        })
    return pd.DataFrame(rows)
