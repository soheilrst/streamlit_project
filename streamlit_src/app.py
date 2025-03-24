import streamlit as st
from campaign_mapping import campaign_map
from streamlit_folium import folium_static
import pandas as pd
from campaign_page import camp_page
from dq_page import dq
import base64
import streamlit.components.v1 as components


def content_box_html(html_content):
    components.html(
        f"""
    <div style="
        background-color: rgba(0, 0, 0, 0.6); 
        padding: 2rem; 
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        font-family: sans-serif;
    ">
        {html_content}
    </div>
    """,
        height=400,
    )


def set_bg_url(url):
    css = f"""
    <style>
    .stApp {{
        background-image: url("{url}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_bg_url("https://raw.githubusercontent.com/soheilrst/streamlit_project/master/streamlit_src/abstract-plexus-blue-geometrical-shapes-connection-ai-generated-image.jpg")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:", ["Home", "Data Quality & Visualisation", "Campaign and Mapping"]
)


if page == "Home":
    content_box_html("""
    <h1>Welcome to the Data Insight Tools</h1>

    <p>
    This platform showcases a collection of focused data projects aimed at improving data quality, enhancing visualization, and enabling geospatial insights.
    </p>

    <p>
    From validating address components to exploring campaign coverage through interactive maps, each section is designed to demonstrate practical solutions to real-world data challenges.
    </p>

    <p>
    Use the sidebar to navigate between the <strong>Data Quality & Visualisation</strong> tools and the <strong>Campaign and Mapping</strong> module.
    </p>
""")



elif page == "Data Quality & Visualisation":

    content_box_html(
        """
        <h1>Data Quality &  Visualisation</h1>
        <h3>Explore the data quality metrics and visualizations in this section.</h3>
        <strong>What You Can Do Here:</strong> 
        <ul><li> Gain insights into the quality and consistency of your postalcode column.(soon also housnumber, street and city)</li>
        <li> Separate street names and house numbers efficiently. </li>
        <li> Compare two house number columns to identify discrepancies.(soon) </li></ul>"""
    )
    dq()


elif page == "Campaign and Mapping":
    content_box_html(
        """
        <h1>Campaign and Mapping</h1>
        <h3>This section provides tools to visualize campaign data on an interactive map.</h3>
        
        <strong>What You Can Do Here:</strong> 
        <ul> 
        <li> View mapped campaigns with relevant data. </li>
        <li> Analyze geographical coverage and campaign distribution. </li>
        </ul> 
        """
    )
    camp_page()
