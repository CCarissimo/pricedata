import streamlit as st

pg = st.navigation([st.Page("article.py"), st.Page("dashboard.py")])
pg.run()