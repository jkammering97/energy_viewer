import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as go
#internal:
from options import *
from content_price import *
from content_production import show_production_content

selected_tab = st.sidebar.radio("Select View", 
["Price View", "Production View"])
st.write("")

# Define the content for Tab 1 and Tab 2 based on the selection
if selected_tab == "Price View":
    show_price_content()
elif selected_tab == "Production View":
    show_production_content()