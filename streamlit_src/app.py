import streamlit as st
from campaign_mapping import campaign_map
from streamlit_folium import folium_static
import pandas as pd
from campaign_page import camp_page

st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:", ["Home", "Data Quality Visualisation", "Campaign and Mapping"]
)


if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the main page content.")

elif page == "Data Quality Visualisation":
    st.title("Data Quality Visualisation")
    st.write("Content for Data Data Quality Visualisation goes here.")
    uploaded_file = st.file_uploader(
        "Choose a file to upload", type=["csv", "xlsx", "parquet"]
    )

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        st.write("Filename:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")


elif page == "Campaign and Mapping":
    
    camp_page()
