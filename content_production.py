import streamlit as st
import eurostat
import matplotlib.pyplot as plt
import base64
import plotly.express as go

def show_production_content():
    st.title("Production Content")

    def display_pdf(pdf_path: str, width: int = 600, height: int = 800):
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"
            st.markdown(f'<iframe src="{pdf_data_url}" width="{width}" height="{height}"></iframe>', unsafe_allow_html=True)
    def main():
        pdf_base_dir = "/Users/joey/Desktop/work/Master/sem1/Technology/Project/Python pdf"
        
        st.title("Energy consumptions")

        options = ["Product", "Sector", "Household", "Transport", "Roadtransport", "Industry"]
        selected_option = st.selectbox("Choose an option:", options)

        radio_options = ["2019", "2020", "2021"]
        selected_radio = st.radio("Select year:", radio_options)

        st.write(f"You are viewing the total energy supply by {selected_option} for the year {selected_radio}")

        if selected_option == "Product":
            pdf_path = f"{pdf_base_dir}/Product {selected_radio}.pdf"

            display_pdf(pdf_path)
        elif selected_option == "Sector":
            pdf_path = f"{pdf_base_dir}/sector {selected_radio}.pdf"
            display_pdf(pdf_path)
        elif selected_option == "Household":
            pdf_path = f"{pdf_base_dir}/households by type of fuel {selected_radio}.pdf"
            display_pdf(pdf_path)
        elif selected_option == "Transport":
            pdf_path = f"{pdf_base_dir}/transport {selected_radio}.pdf"
            display_pdf(pdf_path)
        elif selected_option == "Roadtransport":
            pdf_path = f"{pdf_base_dir}/Project/road {selected_radio}.pdf"
            display_pdf(pdf_path)
        elif selected_option == "Industry":
            pdf_path = f"{pdf_base_dir}/industry {selected_radio}.pdf"
            display_pdf(pdf_path)
    main()
