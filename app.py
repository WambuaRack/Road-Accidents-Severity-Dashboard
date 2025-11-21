import streamlit as st
import pandas as pd 
import plotly.express as px 
import numpy as np 

# Load data
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data("cleaned.csv")

# Streamlit Page Config
st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")
st.title("Road Accidents Severity Dashboard")
st.write("### Rack Visuals")

# Sidebar Filters
filtered = df.copy()
st.sidebar.header("Apply Filters")

# Filter options
day = ["ALL"] + sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day = st.sidebar.selectbox("Day Of The Week", day)

sex = ["ALL"] + sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
selected_sex = st.sidebar.selectbox("Sex Of Driver", sex)

vehicle_type = ["ALL"] + sorted(filtered['Type_of_vehicle'].dropna().unique().tolist())
selected_vehicle = st.sidebar.selectbox("Type of Vehicle", vehicle_type)

owner = ["ALL"] + sorted(filtered['Owner_of_vehicle'].dropna().unique().tolist())
selected_owner = st.sidebar.selectbox("Vehicle Owner", owner)

casualty_sex = ["ALL"] + sorted(filtered['Sex_of_casualty'].dropna().unique().tolist())
selected_casualty = st.sidebar.selectbox("Sex Of Casualty", casualty_sex)

area = ["ALL"] + sorted(filtered['Area_accident_occured'].dropna().unique().tolist())
selected_area = st.sidebar.selectbox("Area Of Occurrence", area)

road_condition = ["ALL"] + sorted(filtered['Road_surface_conditions'].dropna().unique().tolist())
selected_condition = st.sidebar.selectbox("Road Surface Conditions", road_condition)

severity = ["ALL"] + sorted(filtered['Accident_severity'].dropna().unique().tolist())
selected_severity = st.sidebar.selectbox("Accident Severity", severity)

cause = ["ALL"] + sorted(filtered['Cause_of_accident'].dropna().unique().tolist())
selected_cause = st.sidebar.selectbox("Cause Of Accident", cause)

# Apply filters
if selected_day != "ALL":
    filtered = filtered[filtered["Day_of_week"] == selected_day]
if selected_sex != "ALL":
    filtered = filtered[filtered["Sex_of_driver"] == selected_sex]
if selected_vehicle != "ALL":
    filtered = filtered[filtered["Type_of_vehicle"] == selected_vehicle]
if selected_owner != "ALL":
    filtered = filtered[filtered["Owner_of_vehicle"] == selected_owner]
if selected_casualty != "ALL":
    filtered = filtered[filtered["Sex_of_casualty"] == selected_casualty]
if selected_area != "ALL":
    filtered = filtered[filtered["Area_accident_occured"] == selected_area]
if selected_condition != "ALL":
    filtered = filtered[filtered["Road_surface_conditions"] == selected_condition]
if selected_severity != "ALL":
    filtered = filtered[filtered["Accident_severity"] == selected_severity]
if selected_cause != "ALL":
    filtered = filtered[filtered["Cause_of_accident"] == selected_cause]

# Metrics with Deltas
st.write("### Key Metrics")
total_accidents = filtered.shape[0]
total_casualties = int(filtered['Number_of_casualties'].sum())
total_vehicles = int(filtered['Number_of_vehicles_involved'].sum())

# Calculate deltas compared to overall data
delta_accidents = int(total_accidents - df.shape[0])
delta_casualties = int(total_casualties - df['Number_of_casualties'].sum())
delta_vehicles = int(total_vehicles - df['Number_of_vehicles_involved'].sum())

col1, col2, col3 = st.columns(3)
col1.metric("Total Accidents", total_accidents, delta=delta_accidents)
col2.metric("Total Casualties", total_casualties, delta=delta_casualties)
col3.metric("Total Vehicles Involved", total_vehicles, delta=delta_vehicles)

# Charts
st.write("### Visualizations")

# Accident Severity Distribution
fig1 = px.histogram(
    filtered, 
    x='Accident_severity', 
    color='Accident_severity',
    title="Accident Severity Distribution",
    labels={'Accident_severity':'Severity'},
    template='plotly_white'
)
st.plotly_chart(fig1, use_container_width=True)

# Accidents by Day of Week
fig2 = px.histogram(
    filtered,
    x='Day_of_week',
    color='Day_of_week',
    title="Accidents by Day of the Week",
    template='plotly_white'
)
st.plotly_chart(fig2, use_container_width=True)

# Vehicle Type Involved
fig3 = px.histogram(
    filtered,
    x='Type_of_vehicle',
    color='Type_of_vehicle',
    title="Accidents by Vehicle Type",
    template='plotly_white'
)
st.plotly_chart(fig3, use_container_width=True)

# Cause vs Severity Heatmap
cause_severity = pd.crosstab(filtered['Cause_of_accident'], filtered['Accident_severity'])
fig4 = px.imshow(
    cause_severity,
    text_auto=True,
    labels={'x':'Severity', 'y':'Cause of Accident'},
    title='Accident Cause vs Severity',
    aspect='auto'
)
st.plotly_chart(fig4, use_container_width=True)

# Optional: Accidents by Area Map
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    st.write("### Accidents Map")
    map_df = filtered[['Latitude', 'Longitude']].dropna()
    st.map(map_df)

# Filtered Data
st.write("### Filtered Data")
st.dataframe(filtered)

# Download button
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='filtered_accidents.csv',
    mime='text/csv',
)
