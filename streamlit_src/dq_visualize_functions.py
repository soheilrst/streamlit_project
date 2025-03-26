import pandas as pd
import numpy as np
import logging
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go

logger = logging.getLogger()


def visualize(df: pd.DataFrame, col_name: str, counts: list, labels: list) -> None:
    """total_rows = df.shape[0]
    logger.info(f"{total_rows} Eintr\u00e4ge in der Spalte '{col_name}' sind vorhanden.")
    
    critical_total = sum(counts)
    logger.info(f"{critical_total} Eintr\u00e4ge in der Spalte '{col_name}' sind kritisch.")"""

 
    plot_df = pd.DataFrame({
        "Fehlertyp": labels,
        "Anzahl": counts
    }).sort_values("Anzahl", ascending=True)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=plot_df["Anzahl"],
        y=plot_df["Fehlertyp"],
        orientation='h',
        marker=dict(
            color='rgba(0, 123, 255, 0.8)',
            line=dict(color='rgba(255,255,255,0.7)', width=1.5)
        ),
        text=plot_df["Anzahl"],
        textposition='auto',
        textfont=dict(color="white")
       
    ))

    fig.update_layout(
        title=f"Insights zur Spalte '{col_name}'",
        title_font_size=20,
        width=1600,
        height=900,
        xaxis=dict(title="Anzahl", showgrid=False, zeroline=False),
        yaxis=dict(title="Fehlertyp", showgrid=False, automargin=True),
        plot_bgcolor="rgba(0, 0, 0, 0.6)",
        paper_bgcolor="rgba(0, 0, 0, 0.6)",
        font=dict(color="white", size=20),
        margin=dict(t=80, l=200, r=50, b=50)
    )

    
    fig.update_yaxes(tickfont=dict(size=20))
    st.plotly_chart(fig, use_container_width=False)
    return None
    



def plz_visual(df: pd.DataFrame, col: str) -> None:
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].replace("nan", pd.NA)
    
    # disjunkt Bediengungen
    counts = {
    "Fehlender Wert (NaN)": int(df[col].isnull().sum()),

    "Leerzeichen": int(df[col].eq("").sum()),

    "Eintrag enth\u00e4lt 'unbekannt'": int(df[col].str.contains(r"unbekannt", case=False, na=False).sum()),

    "Nicht-numerische Zeichen": int(df[col].fillna("").str.strip().str.contains(r"^(?!.*unbekannt).*[^0-9\s].*", na=False).sum()),

    "Besteht nur aus Nullen": 
        int((df[col].str.match(r"^0+$", na=False) & (df[col].str.len() != 5)).sum()),

    "Startet mit 0 aber 5-stellig":
        int((df[col].str.startswith("0") & (df[col].str.len() == 5) & ~df[col].str.match(r"^0+$")).sum()),

    "Ung\u00fcltige L\u00e4nge": 
        int(((df[col].str.len() != 5) & df[col].str.isdigit() & ~df[col].str.match(r"^0+$")).sum())
}

    visualize(df, col, list(counts.values()), list(counts.keys()))
    return None


