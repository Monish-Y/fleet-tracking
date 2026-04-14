import streamlit as st
import requests
import pandas as pd
import time

Base_URL = "http://127.0.0.1:8000"

st.title("Fleet Tracking Dashboard")
st.write("Hello, World!")

placeholder = st.empty()

from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=None, key="refresh")


data = []

for vid in [1,2,3]:
    try:
        res = requests.get(f"{Base_URL}/vehicle/{vid}")
        if res.status_code == 200:
            vehicle = res.json()
            data.append({"id":vid,"lat":vehicle["latitude"],
                         "lon":vehicle["longitude"]})
    except:
        pass

if data:
    df = pd.DataFrame(data)

    with placeholder.container():
        st.map(df)
        st.dataframe(df)

time.sleep(2)






# st.title("🚀 Streamlit Test App")
#
# # Simple text
# st.write("If you see this, Streamlit is working!")
#
# # Sample data
# data = pd.DataFrame({
#     "lat": [13.0827, 12.9716, 11.0168],
#     "lon": [80.2707, 77.5946, 76.9558]
# })
#
# st.write("Sample Data:")
# st.write(data)
#
# # Map test
# st.write("Map Test:")
# st.map(data)


