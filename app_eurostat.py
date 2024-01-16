import streamlit as st
from options import *
from content_price import *
from content_production import show_production_content

selected_tab = st.sidebar.radio("Select View", 
["Price View", "Production View"])
st.write("")

if selected_tab == "Price View":
    show_price_content()
elif selected_tab == "Production View":
    show_production_content()