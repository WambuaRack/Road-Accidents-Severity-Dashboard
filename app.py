import streamlit as st
import pandas as pd 
import plotly.express as px 
import numpy as np 

@st.cache_data
def load_data(path):
    df =pd.read_csv(path)
    return df


df=load_data("cleaned.csv")
st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")

st.title("Road Accidents Severity  Dashboard")
st.write("### Rack Visuals")

## filter data

filtered =df.copy()
st.sidebar.header( " Apply Filters")
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

sex =["ALL"]+sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
selected_sex =st.sidebar.selectbox("Sex Of Driver  ", sex)

Type_of_vehicle =["ALL"]+sorted(filtered['Type_of_vehicle'].dropna().unique().tolist())
selected_Vehicle =st.sidebar.selectbox("Type of Vehicle", Type_of_vehicle)

Owner_of_vehicle =["ALL"]+sorted(filtered['Owner_of_vehicle'].dropna().unique().tolist())
selected_owner =st.sidebar.selectbox("Vehicle Owner", Owner_of_vehicle)

sex_of_casuality =["ALL"]+sorted(filtered['Sex_of_casualty'].dropna().unique().tolist())
selected_casuality =st.sidebar.selectbox("Sex Of Casuality ", sex_of_casuality)

Area_accident_occured =["ALL"]+sorted(filtered['Area_accident_occured'].dropna().unique().tolist())
selected_area =st.sidebar.selectbox("Area Of Occurence", Area_accident_occured)

Road_surface_conditions =["ALL"]+sorted(filtered['Road_surface_conditions'].dropna().unique().tolist())
selected_condition =st.sidebar.selectbox("Road surface conditions", Road_surface_conditions)

Accident_severity =["ALL"]+sorted(filtered['Accident_severity'].dropna().unique().tolist())
selected_severe =st.sidebar.selectbox("Accident Severity", Accident_severity)

Cause_of_accident =["ALL"]+sorted(filtered['Cause_of_accident'].dropna().unique().tolist())
selected_cause =st.sidebar.selectbox("Cause Of Accident", Cause_of_accident)

## appplying filters 


if selected_day != "ALL":
    filtered = filtered[filtered["Day_of_week"] == selected_day]

if selected_sex != "ALL":
    filtered = filtered[filtered["Sex_of_driver"] == selected_sex]

if selected_Vehicle != "ALL":
    filtered = filtered[filtered["Type_of_vehicle"] == selected_Vehicle]

if selected_owner != "ALL":
    filtered = filtered[filtered["Owner_of_vehicle"] == selected_owner]

if selected_casuality != "ALL":
    filtered = filtered[filtered["Sex_of_casualty"] == selected_casuality]

if selected_area != "ALL":
    filtered = filtered[filtered["Area_accident_occured"] == selected_area]

if selected_condition != "ALL":
    filtered = filtered[filtered["Road_surface_conditions"] == selected_condition]

if selected_severe != "ALL":
    filtered = filtered[filtered["Accident_severity"] == selected_severe]

if selected_cause != "ALL":
    filtered = filtered[filtered["Cause_of_accident"] == selected_cause]