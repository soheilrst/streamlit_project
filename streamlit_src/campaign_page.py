import streamlit as st
from campaign_mapping import campaign_map
from streamlit_folium import folium_static
import pandas as pd

def camp_page():
    st.write("Upload a CSV, Excel, or Parquet file to display campaign data on a map.")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "parquet"])

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith(".parquet"):
            df = pd.read_parquet(uploaded_file)

        st.write("Data Preview:")
        st.write(df.head())

        if "LAT" in df.columns and "LON" in df.columns:

            df = df[(df["LAT"].notna() & df["LON"].notna())]

            city_column = st.selectbox("Select the column for city", df.columns)
            campaign_column = st.selectbox("Select the column for campaign", df.columns)
            selected_city = st.selectbox("Choose a city", df[city_column].unique())
            campaign1 = st.selectbox("Select campaign1", df[campaign_column].unique())
            campaign2 = st.selectbox("Select campaign2", df[campaign_column].unique())

            filtered_df = df[
                (df[city_column].str.contains(selected_city, case=False, na=False))
                & (df[campaign_column].isin({campaign1, campaign2}))
            ]

            if not filtered_df.empty:
                st.write(f"Showing campaigns for {selected_city}")
                m = campaign_map(
                    filtered_df, campaign_column, campaign1, campaign_column, campaign2
                )

                folium_static(m)
            else:
                st.write("No data available for the selected city and campaigns.")
        else:
            st.error("The uploaded file must contain 'LAT' and 'LON' columns.")
    return None