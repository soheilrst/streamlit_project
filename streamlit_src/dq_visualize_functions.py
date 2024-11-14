import pandas as pd
import numpy as np
import logging
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

logger = logging.getLogger()


def visualize(df: pd.DataFrame, col_name: str, counts: list, patterns: list) -> None:
    size = df.shape[0]
    logger.info(f"{size} Eintraege in die column {col_name} sind vorhanden.")
    total_count = sum(int(x) for x in counts)
    logger.info(f"{total_count} Eintraege in die column {col_name} sind Kritisch.")

    plt.figure(figsize=(10, 6))
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})

    sorted_data = sorted(zip(counts, patterns), reverse=True)
    counts, patterns = zip(*sorted_data)

    palette = sns.color_palette("Blues_r", len(patterns))

    sns.barplot(x=list(counts), y=list(patterns), palette=palette)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Anzahl")
    plt.ylabel("Muester")
    plt.title(f"{col_name} Spalte Insights")
    st.pyplot(plt)
    plt.close()
    return None


def plz_visual(df: pd.DataFrame, postcode: str) -> int:
    counts = []

    na_count = df[df[postcode].isnull()].shape[0]
    counts.append(na_count)

    df = df[df[postcode].notna()]
    df[postcode] = df[postcode].astype(int).astype(str)
    df[postcode] = df[postcode].str.strip()

    unbekannt_pattern = r"(?!).*unbekannt.*"
    unbekannt_pattern_count = df[
        df[postcode].str.contains(unbekannt_pattern, regex=True, na=False, case=False)
    ].shape[0]
    counts.append(unbekannt_pattern_count)

    pattern_komma = "."
    komma_pattern_count = df[
        df[postcode].str.contains(pattern_komma, regex=False, na=False, case=False)
    ].shape[0]
    counts.append(komma_pattern_count)

    pattern_not_digit = r"\b(?!unbekannt\b)\D+\b"
    plz_non_digit_count = df[
        df[postcode].str.contains(pattern_not_digit, regex=True, na=False, case=False)
    ].shape[0]
    counts.append(plz_non_digit_count)

    anfang_zero_count = df[
        (df[postcode].str.len() > 5) & (df[postcode].str.startswith("0"))
    ].shape[0]
    counts.append(anfang_zero_count)

    # leerzeichnen
    leer_count = df[df[postcode] == ""].shape[0]
    counts.append(leer_count)

    # zero
    zero_count = df[(df[postcode] == "^0+$") & (df[postcode].str.len() < 5)].shape[0]
    counts.append(zero_count)

    

    # ungülitige länge
    invalid_length_count = df[
        (df[postcode].str.len() != 0)
        & (df[postcode].str.len() != 5)
        & (df[postcode].str.isdigit())
    ].shape[0]
    counts.append(invalid_length_count)

    patterns = [
        "na",
        "unbekannt",
        "komma",
        "nicht_digit",
        "anfang_zero",
        "leerzeichnen",
        "zero",
        "unguelitige_laenge",
    ]
    visualize(df, postcode, counts, patterns)

    return None