import streamlit as st

pg = st.navigation([st.Page("overview.py"), st.Page("hotel_pricing.py")])
pg.run()