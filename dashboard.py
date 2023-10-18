import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("dadostempo.csv", sep=";", decimal=",")
dl = pd.read_csv("temperatura.csv", sep=";", decimal=",")
df["Category"] = pd.to_datetime(df["Category"], format='%Y')
dl["Ano"] = pd.to_datetime(dl["Ano"], format='%Y')

df["Ano"] = df["Category"].dt.year
dl["Ano"] = dl["Ano"].dt.year 

fig_line = px.line(df, x="Ano", y=["NOAA National Climatic Data Center","NASA Goddard Institute for Space Studies","Japanese Meteorological Agency","Met Office Hadley Centre/Climatic Research Unit"], title="Evolução ao longo dos anos")
fig_lineTemp = px.line(dl, x="Ano", y="Temperatura °C", title="Quadrática")

st.plotly_chart(fig_line)
st.plotly_chart(fig_lineTemp)

month = st.sidebar.selectbox("Ano", df["Ano"].unique())

df_filtered = df[df["Ano"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Category", y=["NOAA National Climatic Data Center","NASA Goddard Institute for Space Studies","Japanese Meteorological Agency","Met Office Hadley Centre/Climatic Research Unit"], title="Por ano")
col1.plotly_chart(fig_date)
