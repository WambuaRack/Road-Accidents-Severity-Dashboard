### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:35:04 PM*

**[REMOVED]**
```
(from line ~74)
total_casualties = filtered['Number_of_casualties'].sum()
total_vehicles = filtered['Number_of_vehicles_involved'].sum()

```
**[ADDED]**
```
74    total_casualties = int(filtered['Number_of_casualties'].sum())
75    total_vehicles = int(filtered['Number_of_vehicles_involved'].sum())
```
**[REMOVED]**
```
(from line ~78)
delta_accidents = total_accidents - df.shape[0]
delta_casualties = total_casualties - df['Number_of_casualties'].sum()
delta_vehicles = total_vehicles - df['Number_of_vehicles_involved'].sum()

```
**[ADDED]**
```
78    delta_accidents = int(total_accidents - df.shape[0])
79    delta_casualties = int(total_casualties - df['Number_of_casualties'].sum())
80    delta_vehicles = int(total_vehicles - df['Number_of_vehicles_involved'].sum())
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:33:29 PM*

**[ADDED]**
```
6     # Load data
```
**[REMOVED]**
```
(from line ~9)
    df =pd.read_csv(path)

```
**[ADDED]**
```
9         df = pd.read_csv(path)
```
**[ADDED]**
```
12    df = load_data("cleaned.csv")
```
**[REMOVED]**
```
(from line ~14)
df=load_data("cleaned.csv")
st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")

st.title("Road Accidents Severity  Dashboard")

```
**[ADDED]**
```
14    # Streamlit Page Config
15    st.set_page_config(page_title="Rack Visuals", page_icon="📊", layout="wide")
16    st.title("Road Accidents Severity Dashboard")
```
**[REMOVED]**
```
(from line ~19)
## filter data

```
**[ADDED]**
```
19    # Sidebar Filters
20    filtered = df.copy()
21    st.sidebar.header("Apply Filters")
```
**[REMOVED]**
```
(from line ~23)
filtered =df.copy()
st.sidebar.header( " Apply Filters")
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
23    # Filter options
24    day = ["ALL"] + sorted(filtered['Day_of_week'].dropna().unique().tolist())
25    selected_day = st.sidebar.selectbox("Day Of The Week", day)
```
**[REMOVED]**
```
(from line ~27)
sex =["ALL"]+sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
selected_sex =st.sidebar.selectbox("Sex Of Driver  ", sex)

```
**[ADDED]**
```
27    sex = ["ALL"] + sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
28    selected_sex = st.sidebar.selectbox("Sex Of Driver", sex)
```
**[REMOVED]**
```
(from line ~30)
Type_of_vehicle =["ALL"]+sorted(filtered['Type_of_vehicle'].dropna().unique().tolist())
selected_Vehicle =st.sidebar.selectbox("Type of Vehicle", Type_of_vehicle)

```
**[ADDED]**
```
30    vehicle_type = ["ALL"] + sorted(filtered['Type_of_vehicle'].dropna().unique().tolist())
31    selected_vehicle = st.sidebar.selectbox("Type of Vehicle", vehicle_type)
```
**[REMOVED]**
```
(from line ~33)
Owner_of_vehicle =["ALL"]+sorted(filtered['Owner_of_vehicle'].dropna().unique().tolist())
selected_owner =st.sidebar.selectbox("Vehicle Owner", Owner_of_vehicle)

```
**[ADDED]**
```
33    owner = ["ALL"] + sorted(filtered['Owner_of_vehicle'].dropna().unique().tolist())
34    selected_owner = st.sidebar.selectbox("Vehicle Owner", owner)
```
**[REMOVED]**
```
(from line ~36)
sex_of_casuality =["ALL"]+sorted(filtered['Sex_of_casualty'].dropna().unique().tolist())
selected_casuality =st.sidebar.selectbox("Sex Of Casuality ", sex_of_casuality)

```
**[ADDED]**
```
36    casualty_sex = ["ALL"] + sorted(filtered['Sex_of_casualty'].dropna().unique().tolist())
37    selected_casualty = st.sidebar.selectbox("Sex Of Casualty", casualty_sex)
```
**[REMOVED]**
```
(from line ~39)
Area_accident_occured =["ALL"]+sorted(filtered['Area_accident_occured'].dropna().unique().tolist())
selected_area =st.sidebar.selectbox("Area Of Occurence", Area_accident_occured)

```
**[ADDED]**
```
39    area = ["ALL"] + sorted(filtered['Area_accident_occured'].dropna().unique().tolist())
40    selected_area = st.sidebar.selectbox("Area Of Occurrence", area)
```
**[REMOVED]**
```
(from line ~42)
Road_surface_conditions =["ALL"]+sorted(filtered['Road_surface_conditions'].dropna().unique().tolist())
selected_condition =st.sidebar.selectbox("Road surface conditions", Road_surface_conditions)

```
**[ADDED]**
```
42    road_condition = ["ALL"] + sorted(filtered['Road_surface_conditions'].dropna().unique().tolist())
43    selected_condition = st.sidebar.selectbox("Road Surface Conditions", road_condition)
```
**[REMOVED]**
```
(from line ~45)
Accident_severity =["ALL"]+sorted(filtered['Accident_severity'].dropna().unique().tolist())
selected_severe =st.sidebar.selectbox("Accident Severity", Accident_severity)

```
**[ADDED]**
```
45    severity = ["ALL"] + sorted(filtered['Accident_severity'].dropna().unique().tolist())
46    selected_severity = st.sidebar.selectbox("Accident Severity", severity)
```
**[REMOVED]**
```
(from line ~48)
Cause_of_accident =["ALL"]+sorted(filtered['Cause_of_accident'].dropna().unique().tolist())
selected_cause =st.sidebar.selectbox("Cause Of Accident", Cause_of_accident)

```
**[ADDED]**
```
48    cause = ["ALL"] + sorted(filtered['Cause_of_accident'].dropna().unique().tolist())
49    selected_cause = st.sidebar.selectbox("Cause Of Accident", cause)
```
**[REMOVED]**
```
(from line ~51)
## appplying filters 



```
**[ADDED]**
```
51    # Apply filters
```
**[REMOVED]**
```
(from line ~54)


```
**[REMOVED]**
```
(from line ~56)

if selected_Vehicle != "ALL":
    filtered = filtered[filtered["Type_of_vehicle"] == selected_Vehicle]


```
**[ADDED]**
```
56    if selected_vehicle != "ALL":
57        filtered = filtered[filtered["Type_of_vehicle"] == selected_vehicle]
```
**[REMOVED]**
```
(from line ~60)

if selected_casuality != "ALL":
    filtered = filtered[filtered["Sex_of_casualty"] == selected_casuality]


```
**[ADDED]**
```
60    if selected_casualty != "ALL":
61        filtered = filtered[filtered["Sex_of_casualty"] == selected_casualty]
```
**[REMOVED]**
```
(from line ~64)


```
**[ADDED]**
```
66    if selected_severity != "ALL":
67        filtered = filtered[filtered["Accident_severity"] == selected_severity]
68    if selected_cause != "ALL":
69        filtered = filtered[filtered["Cause_of_accident"] == selected_cause]
```
**[REMOVED]**
```
(from line ~71)
if selected_severe != "ALL":
    filtered = filtered[filtered["Accident_severity"] == selected_severe]

```
**[ADDED]**
```
71    # Metrics with Deltas
72    st.write("### Key Metrics")
73    total_accidents = filtered.shape[0]
74    total_casualties = filtered['Number_of_casualties'].sum()
75    total_vehicles = filtered['Number_of_vehicles_involved'].sum()
```
**[REMOVED]**
```
(from line ~77)
if selected_cause != "ALL":
    filtered = filtered[filtered["Cause_of_accident"] == selected_cause]
```
**[ADDED]**
```
77    # Calculate deltas compared to overall data
78    delta_accidents = total_accidents - df.shape[0]
79    delta_casualties = total_casualties - df['Number_of_casualties'].sum()
80    delta_vehicles = total_vehicles - df['Number_of_vehicles_involved'].sum()
81    
82    col1, col2, col3 = st.columns(3)
83    col1.metric("Total Accidents", total_accidents, delta=delta_accidents)
84    col2.metric("Total Casualties", total_casualties, delta=delta_casualties)
85    col3.metric("Total Vehicles Involved", total_vehicles, delta=delta_vehicles)
86    
87    # Charts
88    st.write("### Visualizations")
89    
90    # Accident Severity Distribution
91    fig1 = px.histogram(
92        filtered, 
93        x='Accident_severity', 
94        color='Accident_severity',
95        title="Accident Severity Distribution",
96        labels={'Accident_severity':'Severity'},
97        template='plotly_white'
98    )
99    st.plotly_chart(fig1, use_container_width=True)
100   
101   # Accidents by Day of Week
102   fig2 = px.histogram(
103       filtered,
104       x='Day_of_week',
105       color='Day_of_week',
106       title="Accidents by Day of the Week",
107       template='plotly_white'
108   )
109   st.plotly_chart(fig2, use_container_width=True)
110   
111   # Vehicle Type Involved
112   fig3 = px.histogram(
113       filtered,
114       x='Type_of_vehicle',
115       color='Type_of_vehicle',
116       title="Accidents by Vehicle Type",
117       template='plotly_white'
118   )
119   st.plotly_chart(fig3, use_container_width=True)
120   
121   # Cause vs Severity Heatmap
122   cause_severity = pd.crosstab(filtered['Cause_of_accident'], filtered['Accident_severity'])
123   fig4 = px.imshow(
124       cause_severity,
125       text_auto=True,
126       labels={'x':'Severity', 'y':'Cause of Accident'},
127       title='Accident Cause vs Severity',
128       aspect='auto'
129   )
130   st.plotly_chart(fig4, use_container_width=True)
131   
132   # Optional: Accidents by Area Map
133   if 'Latitude' in df.columns and 'Longitude' in df.columns:
134       st.write("### Accidents Map")
135       map_df = filtered[['Latitude', 'Longitude']].dropna()
136       st.map(map_df)
137   
138   # Filtered Data
139   st.write("### Filtered Data")
140   st.dataframe(filtered)
141   
142   # Download button
143   csv = filtered.to_csv(index=False).encode('utf-8')
144   st.download_button(
145       label="Download CSV",
146       data=csv,
147       file_name='filtered_accidents.csv',
148       mime='text/csv',
149   )
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:31:14 PM*

**[REMOVED]**
```
(from line ~52)
if selected_area !="ALL":
    filtered =filtered[filtered["Area_accident_occured"] == selected_area]
    
    
```
**[ADDED]**
```
52    if selected_day != "ALL":
53        filtered = filtered[filtered["Day_of_week"] == selected_day]
54    
55    if selected_sex != "ALL":
56        filtered = filtered[filtered["Sex_of_driver"] == selected_sex]
57    
58    if selected_Vehicle != "ALL":
59        filtered = filtered[filtered["Type_of_vehicle"] == selected_Vehicle]
60    
61    if selected_owner != "ALL":
62        filtered = filtered[filtered["Owner_of_vehicle"] == selected_owner]
63    
64    if selected_casuality != "ALL":
65        filtered = filtered[filtered["Sex_of_casualty"] == selected_casuality]
66    
67    if selected_area != "ALL":
68        filtered = filtered[filtered["Area_accident_occured"] == selected_area]
69    
70    if selected_condition != "ALL":
71        filtered = filtered[filtered["Road_surface_conditions"] == selected_condition]
72    
73    if selected_severe != "ALL":
74        filtered = filtered[filtered["Accident_severity"] == selected_severe]
75    
76    if selected_cause != "ALL":
77        filtered = filtered[filtered["Cause_of_accident"] == selected_cause]
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:30:15 PM*

**[ADDED]**
```
49    ## appplying filters 
50    
51    
52    if selected_area !="ALL":
53        filtered =filtered[filtered["Area_accident_occured"] == selected_area]
54        
55        
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:27:16 PM*

**[REMOVED]**
```
(from line ~34)
sex =["ALL"]+sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
selected_sex =st.sidebar.selectbox("Sex ", sex)

```
**[ADDED]**
```
34    sex_of_casuality =["ALL"]+sorted(filtered['Sex_of_casualty'].dropna().unique().tolist())
35    selected_casuality =st.sidebar.selectbox("Sex Of Casuality ", sex_of_casuality)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:26:12 PM*

**[REMOVED]**
```
(from line ~26)
selected_sex =st.sidebar.selectbox("Sex", sex)

```
**[ADDED]**
```
26    selected_sex =st.sidebar.selectbox("Sex Of Driver  ", sex)
```
**[ADDED]**
```
34    sex =["ALL"]+sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
35    selected_sex =st.sidebar.selectbox("Sex ", sex)
36    
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:24:42 PM*

**[REMOVED]**
```
(from line ~43)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
43    Cause_of_accident =["ALL"]+sorted(filtered['Cause_of_accident'].dropna().unique().tolist())
44    selected_cause =st.sidebar.selectbox("Cause Of Accident", Cause_of_accident)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:24:06 PM*

**[REMOVED]**
```
(from line ~40)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
40    Accident_severity =["ALL"]+sorted(filtered['Accident_severity'].dropna().unique().tolist())
41    selected_severe =st.sidebar.selectbox("Accident Severity", Accident_severity)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:23:18 PM*

**[REMOVED]**
```
(from line ~37)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
37    Road_surface_conditions =["ALL"]+sorted(filtered['Road_surface_conditions'].dropna().unique().tolist())
38    selected_condition =st.sidebar.selectbox("Road surface conditions", Road_surface_conditions)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:21:46 PM*

**[REMOVED]**
```
(from line ~34)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
34    Area_accident_occured =["ALL"]+sorted(filtered['Area_accident_occured'].dropna().unique().tolist())
35    selected_area =st.sidebar.selectbox("Area Of Occurence", Area_accident_occured)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:21:04 PM*

**[REMOVED]**
```
(from line ~31)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
31    Owner_of_vehicle =["ALL"]+sorted(filtered['Owner_of_vehicle'].dropna().unique().tolist())
32    selected_owner =st.sidebar.selectbox("Vehicle Owner", Owner_of_vehicle)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:20:26 PM*

**[REMOVED]**
```
(from line ~26)
selected_day =st.sidebar.selectbox("Sex", sex)

```
**[ADDED]**
```
26    selected_sex =st.sidebar.selectbox("Sex", sex)
```
**[REMOVED]**
```
(from line ~28)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
28    Type_of_vehicle =["ALL"]+sorted(filtered['Type_of_vehicle'].dropna().unique().tolist())
29    selected_Vehicle =st.sidebar.selectbox("Type of Vehicle", Type_of_vehicle)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:19:25 PM*

**[REMOVED]**
```
(from line ~26)
selected_day =st.sidebar.selectbox("Day Of The Week", sex)

```
**[ADDED]**
```
26    selected_day =st.sidebar.selectbox("Sex", sex)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:19:12 PM*

**[REMOVED]**
```
(from line ~25)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
selected_day =st.sidebar.selectbox("Day Of The Week", day)

```
**[ADDED]**
```
25    sex =["ALL"]+sorted(filtered['Sex_of_driver'].dropna().unique().tolist())
26    selected_day =st.sidebar.selectbox("Day Of The Week", sex)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:18:26 PM*

**[ADDED]**
```
25    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
26    selected_day =st.sidebar.selectbox("Day Of The Week", day)
27    
28    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
29    selected_day =st.sidebar.selectbox("Day Of The Week", day)
30    
31    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
32    selected_day =st.sidebar.selectbox("Day Of The Week", day)
33    
34    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
35    selected_day =st.sidebar.selectbox("Day Of The Week", day)
36    
37    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
38    selected_day =st.sidebar.selectbox("Day Of The Week", day)
39    
40    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
41    selected_day =st.sidebar.selectbox("Day Of The Week", day)
42    
43    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
44    selected_day =st.sidebar.selectbox("Day Of The Week", day)
45    
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:17:43 PM*

**[REMOVED]**
```
(from line ~22)
day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().toist())

```
**[ADDED]**
```
22    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().tolist())
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:17:31 PM*

**[REMOVED]**
```
(from line ~22)
day =["ALL"]+sort(filtered['Day_of_week'].dropna().unique().toList())

```
**[ADDED]**
```
22    day =["ALL"]+sorted(filtered['Day_of_week'].dropna().unique().toist())
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:17:18 PM*

**[REMOVED]**
```
(from line ~21)
st.sidebar.header( "## Apply Filters")
day =["ALL"]+sort(filtered['Day_of_week'].dropna().unique().tolist())

```
**[ADDED]**
```
21    st.sidebar.header( " Apply Filters")
22    day =["ALL"]+sort(filtered['Day_of_week'].dropna().unique().toList())
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:16:59 PM*

**[ADDED]**
```
21    st.sidebar.header( "## Apply Filters")
22    day =["ALL"]+sort(filtered['Day_of_week'].dropna().unique().tolist())
23    selected_day =st.sidebar.selectbox("Day Of The Week", day)
```
**[REMOVED]**
```
(from line ~25)
day =filtered['Day_of_week'].sort


```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:14:07 PM*

**[REMOVED]**
```
(from line ~22)
day =filtered['']

```
**[ADDED]**
```
22    day =filtered['Day_of_week'].sort
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:13:49 PM*

**[ADDED]**
```
22    day =filtered['']
```
**[REMOVED]**
```
(from line ~24)


```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:13:12 PM*

**[ADDED]**
```
18    ## filter data
19    
20    filtered =df.copy()
21    
22    
23    
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:12:37 PM*

**[REMOVED]**
```
(from line ~16)
st.write("Rack Visuals")

```
**[ADDED]**
```
16    st.write("### Rack Visuals")
17    
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:11:59 PM*

**[REMOVED]**
```
(from line ~15)
st.title("Road Accidents Severity  Dashboard")
```
**[ADDED]**
```
15    st.title("Road Accidents Severity  Dashboard")
16    st.write("Rack Visuals")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:11:17 PM*

**[REMOVED]**
```
(from line ~15)
st.title()
```
**[ADDED]**
```
15    st.title("Road Accidents Severity  Dashboard")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:11:01 PM*

**[REMOVED]**
```
(from line ~13)
st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")
```
**[ADDED]**
```
13    st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")
14    
15    st.title()
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:10:13 PM*

**[REMOVED]**
```
(from line ~13)
st.set_page_config(page_title="Rack visuals", page_icon="analysis.png", layout="wide")
```
**[ADDED]**
```
13    st.set_page_config(page_title="Rack Visuals", page_icon="analysis.png", layout="wide")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:09:49 PM*

**[REMOVED]**
```
(from line ~13)
st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png", layout="wide")
```
**[ADDED]**
```
13    st.set_page_config(page_title="Rack visuals", page_icon="analysis.png", layout="wide")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:09:26 PM*

**[REMOVED]**
```
(from line ~13)
st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png")
```
**[ADDED]**
```
13    st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png", layout="wide")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:08:41 PM*

**[REMOVED]**
```
(from line ~13)
 st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png")
```
**[ADDED]**
```
13    st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:07:26 PM*

**[REMOVED]**
```
(from line ~13)
 st.set_page_config(page_title="")
```
**[ADDED]**
```
13     st.set_page_config(page_title="Road Accidents Severity Dashboard", page_icon="analysis.png")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:06:51 PM*

**[REMOVED]**
```
(from line ~13)
 st.set_page_config(page_title='<a href="https://www.flaticon.com/free-icons/analysis" title="analysis icons">Analysis icons created by RaftelDesign - Flaticon</a>')
```
**[ADDED]**
```
13     st.set_page_config(page_title="")
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:05:49 PM*

**[REMOVED]**
```
(from line ~13)
 st.set_page_config(page_title=)
```
**[ADDED]**
```
13     st.set_page_config(page_title='<a href="https://www.flaticon.com/free-icons/analysis" title="analysis icons">Analysis icons created by RaftelDesign - Flaticon</a>')
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:04:49 PM*

**[REMOVED]**
```
(from line ~13)
st.dataframe(df)
```
**[ADDED]**
```
13     st.set_page_config(page_title=)
```

---

### 📄 c:\Users\Administrator\Desktop\Road Accidents Severity\app.py
*Saved at: 11/21/2025, 8:02:52 PM*

**[ADDED]**
```
1     import streamlit as st
2     import pandas as pd 
3     import plotly.express as px 
4     import numpy as np 
5     
6     @st.cache_data
7     def load_data(path):
8         df =pd.read_csv(path)
9         return df
10    
11    
12    df=load_data("cleaned.csv")
13    st.dataframe(df)
```

---

