import streamlit as st
from campaign_mapping import campaign_map
from streamlit_folium import folium_static
import pandas as pd
from campaign_page import camp_page
from dq_page import dq

st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:", ["Home", "Data Quality Visualisation", "Campaign and Mapping"]
)


if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the main page content.")

elif page == "Data Quality Visualisation":
    dq()
    

elif page == "Campaign and Mapping":
    
    camp_page()
