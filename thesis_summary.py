import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer

pdf_viewer(
    input="./thesis_extended_abstract.pdf",
    width=700,
    zoom_level="auto"
)
