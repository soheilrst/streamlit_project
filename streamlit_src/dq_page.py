from logging import PlaceHolder
import streamlit as st
import numpy as np
from dq_functions import *
from dq_visualize_functions import *
from streamlit_folium import folium_static
import pandas as pd
import openpyxl
from io import BytesIO


def dq() -> None:

    uploaded_file = st.file_uploader(
        "Choose a file to upload", type=["csv", "xlsx", "parquet"]
    )

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
        df = df.dropna(axis="columns", how="all")
        st.write("Data Preview:")
        st.write("File shape:", df.shape)
        st.write(df.head())

        option = st.selectbox(
            "Choose an operation",
            ["Separate Street and House Number", "Visualize Data Quality"],
        )

        if option == "Separate Street and House Number":
            col_name = str(
                st.text_input(
                    "Enter the column name containing street and house number"
                )
            )
            new_street_col = str(
                st.text_input("Enter the new column name for Street", "Street")
            )
            new_hsnr_col = str(
                st.text_input(
                    "Enter the new column name for House Number", "House Number"
                )
            )

            if col_name:

                if col_name in df.columns:
                    df[new_street_col] = df[col_name].apply(extract_street_name)
                    df[new_hsnr_col] = df[col_name].apply(extract_house_number)
                    st.write("Updated DataFrame:")
                    st.dataframe(df.head())

                    output_format_option = st.selectbox(
                        "Choose an Output Format", ["Parquet", "Excel", "CSV"]
                    )

                    if output_format_option == "Parquet":
                        output = BytesIO()
                        df.to_parquet(output, index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as Parquet",
                            data=output,
                            file_name="processed_data.parquet",
                            mime="application/octet-stream",
                        )
                    elif output_format_option == "Excel":
                        output = BytesIO()
                        df.to_excel(output, engine="openpyxl", index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as Excel",
                            data=output,
                            file_name="processed_data.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        )
                    elif output_format_option == "CSV":
                        output = BytesIO()
                        df.to_csv(output, index=False)
                        output.seek(0)
                        st.download_button(
                            label="Download processed data as CSV",
                            data=output,
                            file_name="processed_data.csv",
                            mime="text/csv",
                        )
                else:

                    st.error(
                        "The specified column name does not exist in the DataFrame!"
                    )

        elif option == "Visualize Data Quality":
            st.write("Data quality visualizations and analysis would go here.")
            col_name = str(st.text_input("Enter the column name containing Postalcode"))
            if col_name:
                if col_name not in df.columns:

                    st.error(
                        "The specified column name does not exist in the DataFrame!"
                    )

                plz_check = plz_visual(df, col_name)

            else:
                st.info("Please choose a give the Postalcode Column name.")

    else:
        df = pd.read_excel("https://raw.githubusercontent.com/soheilrst/streamlit_project/master/streamlit_src/Data/OSM_Berlin_DQ.xlsx", engine="openpyxl")
        
        st.write("Example Data Preview:")
        st.write("File shape:", df.shape)
        st.write(df.head())

        option = st.selectbox(
            "Choose an operation",
            ["Visualize Data Quality", "Separate Street and House Number"],
        )

        plz_check = plz_visual(df, "POSTALCODE")

    return None
