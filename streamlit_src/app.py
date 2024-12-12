import streamlit as st
from campaign_mapping import campaign_map
from streamlit_folium import folium_static
import pandas as pd
from campaign_page import camp_page
from dq_page import dq
import base64


st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:", ["Home", "Data Quality & Visualisation", "Campaign and Mapping"]
)


if page == "Home":
    st.title("Welcome to the Home Page")
    st.write(
        """Hey there! Thanks for visiting my website. I'm excited to share some small but cool data analysis 
            projects because I'm passionate about data and how it can uncover business insights and make life easier for everyone.
            From data quality tools to visualizations and mapping projects, I'm here to have fun with data and I hope you do too. Enjoy exploring!"""
    )

    st.info(
        "Navigate using the sidebar to explore the Data Quality & Visualisation or the Campaign and Mapping sections."
    )


elif page == "Data Quality & Visualisation":
    st.title("Data Quality &  Visualisation")
    st.write("Explore the data quality metrics and visualizations in this section.")
    st.markdown(
        """
        ### What You Can Do Here:
        - Gain insights into the quality and consistency of your postalcode column.(soon also housnumber, street and city)
        - Separate street names and house numbers efficiently.
        - Compare two house number columns to identify discrepancies.(soon)"""
    )
    dq()


elif page == "Campaign and Mapping":
    st.title("Campaign and Mapping")
    st.write(
        "This section provides tools to visualize campaign data on an interactive map."
    )
    st.markdown(
        """
        ### What You Can Do Here:
        - View mapped campaigns with relevant data.
        - Analyze geographical coverage and campaign distribution.
        """
    )
    camp_page()
