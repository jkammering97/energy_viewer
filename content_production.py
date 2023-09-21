import streamlit as st
import base64
import os

def show_production_content():
    st.title("Production Content")

    def display_pdf(pdf_path: str, width: int = 600, height: int = 800):
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"
            st.markdown(f'<iframe src="{pdf_data_url}" width="{width}" height="{height}" type="application/pdf"></iframe>',
                        unsafe_allow_html=True)
    
    def main():
        pdf_base_dir = os.path.join(os.getcwd(), "PDFs")
        st.title("Energy consumptions")

        options = ["Product", "Sector", "Household", "Transport", "Roadtransport", "Industry"]
        selected_option = st.selectbox("Choose an option:", options)

        radio_options = ["2019", "2020", "2021"]
        selected_radio = st.radio("Select year:", radio_options)

        st.write(f"You are viewing the total energy supply by {selected_option} for the year {selected_radio}")

        pdf_file_mapping = {
        "Product": f"Product {selected_radio}.pdf",
        "Sector": f"sector {selected_radio}.pdf",
        "Household": f"households by type of fuel {selected_radio}.pdf",
        "Transport": f"transport {selected_radio}.pdf",
        "Roadtransport": f"road {selected_radio}.pdf",
        "Industry": f"industry {selected_radio}.pdf"
        }

        pdf_file_name = pdf_file_mapping.get(selected_option)

        if pdf_file_name:
            pdf_path = os.path.join(pdf_base_dir, pdf_file_name)
            display_pdf(pdf_path)
        else:
            st.error("Selected option not recognized.")

    main()
