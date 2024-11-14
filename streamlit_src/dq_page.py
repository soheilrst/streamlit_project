from logging import PlaceHolder
import streamlit as st
import numpy as np
from dq_functions import *
from streamlit_folium import folium_static
import pandas as pd
import openpyxl
from io import BytesIO

def dq() -> None: 
    st.title("Data Quality & Visualisation")
    st.write("Content for Data Quality & Data Visualisation goes here.")
    
    uploaded_file = st.file_uploader("Choose a file to upload", type=["csv", "xlsx", "parquet"])
    
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write("Filename:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")
        
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, delimiter=",")
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        elif uploaded_file.name.endswith(".parquet"):
            df = pd.read_parquet(uploaded_file)
        
        
        df = df.replace(to_replace="None", value=np.nan)
        df = df.dropna(axis="columns", how='all')
        st.write("Data Preview:")
        st.write(df.head())
        
        
        option = st.selectbox("Choose an operation", ["Separate Street and House Number", "Visualize Data Quality"])
        
        if option == "Separate Street and House Number":
            col_name = str(st.text_input("Enter the column name containing street and house number"))
            new_street_col = str(st.text_input("Enter the new column name for Street", "Street"))
            new_hsnr_col = str(st.text_input("Enter the new column name for House Number", "House Number"))
            
            if col_name:
                
                if col_name in df.columns:
                    df[new_street_col] = df[col_name].apply(extract_street_name)
                    df[new_hsnr_col] = df[col_name].apply(extract_house_number)
                    st.write("Updated DataFrame:")
                    st.dataframe(df.head())
                    
              
                    output_format_option = st.selectbox("Choose an Output Format", ["Parquet", "Excel", "CSV"])
                    
                    
                    if output_format_option == "Parquet":
                        output = BytesIO()
                        df.to_parquet(output, index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as Parquet",
                            data=output,
                            file_name='processed_data.parquet',
                            mime='application/octet-stream',
                        )
                    elif output_format_option == "Excel":
                        output = BytesIO()
                        df.to_excel(output, engine="openpyxl", index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as Excel",
                            data=output,
                            file_name='processed_data.xlsx',
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        )
                    elif output_format_option == "CSV":
                        output = BytesIO()
                        df.to_csv(output, index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as CSV",
                            data=output,
                            file_name='processed_data.csv',
                            mime='text/csv',
                        )
                else:
                    
                    st.error("The specified column name does not exist in the DataFrame!")
                    
        elif option == "Visualize Data Quality":
            st.write("Data quality visualizations and analysis would go here.")
        
    else:
        st.info("Please choose a file to upload.")
        
    return None
                
                
            
            
          