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

