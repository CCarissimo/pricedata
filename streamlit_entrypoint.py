import streamlit as st

pg = st.navigation([st.Page("overview.py"), st.Page("hotel_pricing.py"), st.Page("videos.py")])
pg.run()
