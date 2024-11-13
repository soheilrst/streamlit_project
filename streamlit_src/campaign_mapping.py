import pandas as pd
from typing import List, Dict
import folium
from folium.plugins import MarkerCluster
from pyproj import Proj, transform


def convert_coordinates(row):
    in_proj = Proj(init="epsg:25832")
    out_proj = Proj(init="epsg:4326")
    lon, lat = transform(in_proj, out_proj, row["LON"], row["LAT"])
    return pd.Series([lat, lon], index=["LATITUDE", "LONGITUDE"])


def campaign_map(
    df: pd.DataFrame, tag_name1: str, key1: str, tag_name2: str, key2: str
) -> folium.Map:

    m = folium.Map(location=[52.52, 13.405], zoom_start=12)

    cluster1 = MarkerCluster(name=key1).add_to(m)
    cluster2 = MarkerCluster(name=key2).add_to(m)

    for _, row in df.iterrows():

        if row[tag_name1] == key1:
            folium.Marker(
                location=[row["LAT"], row["LON"]],
                popup=f"<br>(Companyname): {row['COMPANYNAME']}",
                icon=folium.Icon(color="red"),
            ).add_to(cluster1)

        elif row[tag_name2] == key2:
            folium.Marker(
                location=[row["LAT"], row["LON"]],
                popup=f"<br>(Companyname): {row['COMPANYNAME']}",
                icon=folium.Icon(color="blue"),
            ).add_to(cluster2)

    folium.LayerControl().add_to(m)
    return m
