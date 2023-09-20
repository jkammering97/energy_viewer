import streamlit as st
import eurostat
from options import *
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def show_price_content():

    def request_data_df(code: str,
                        country: str,
                        year_from: int):
        # pars = eurostat.get_pars(code)
        # par_values = eurostat.get_par_values(code, 'geo')
        my_filter_pars = {'startPeriod': year_from,
                        'geo': country}
        df = eurostat.get_data_df(code, filter_pars=my_filter_pars)
        df = df[df.currency=='EUR']
        numerical_columns = [col for col in df.columns if col.startswith('20')]
        df = df.drop('nrg_prc', axis=1)
        df = df.groupby('nrg_cons')[numerical_columns].sum().reset_index()
        return df

    # nrg = eurostat.get_data_df(code="NRG_PC_204", filter_pars={'startPeriod': 2015, 'geo': "SE"})
    # nrg[nrg.currency=='EUR']
    # nrg2 = nrg[nrg.currency=="EUR"]
    # nrg2[nrg2['tax']=="X_TAX"]

    statistics = {#"Final energy consumption in households by type of fuel": "TEN00125",
    "Electricity prices for non-household consumers": "NRG_PC_205_C",
    "Electricity prices for household consumers": "NRG_PC_204_C"}

    st.title("Welcome to EnergyView")
    st.write("Please choose a country below to see your statistic.")

    selected_statistic = st.sidebar.selectbox("select a statistic:",
                                    options= statistics.keys(),
                                    index= 0,
                                    key= "stat_select")

    # years = [2017, 2018, 2019, 2020, 2021, 2022]
    year_from = st.sidebar.slider("select from which year on to collect:",
    2015,
    2022)

    selected_countries = st.multiselect("Select Countries", country_iso2_mapping)
    fig = px.line()

    dfs = []
    for country in selected_countries:
        try:
            data1 = request_data_df(code= statistics[selected_statistic],
                                    country= country_iso2_mapping[country],
                                    year_from= year_from)
            data1['country'] = country
            dfs.append(data1)
        except BaseException:
            pass
            st.warning(f'{country} is not available',icon="🚨")

    if dfs: 
        merged_df = pd.concat(dfs, ignore_index=True)
        df_melted = pd.melt(merged_df, id_vars=['country', 'nrg_cons'], var_name='Year', value_name='Value [€/kWh]')
  
        if not df_melted.empty:
            constants = df_melted['nrg_cons'].unique()
            # st.write(constants)
            selected_constant = st.sidebar.selectbox("choose a kWh consumption category:",
                        options= constants,
                        index= 0,
                        key= "const_select")

            st.sidebar.markdown(custom_css, unsafe_allow_html=True)
            st.sidebar.markdown(legend_content, unsafe_allow_html=True)

            if selected_constant:

                merged_df = merged_df[merged_df['nrg_cons']==selected_constant]
                df_long = merged_df.melt(id_vars="country", var_name="Year", value_name="Value [€/kWh]")
                df_long = df_long.sort_values(by="Year")  # Sort the DataFrame by "Year"
                

                fig = px.line(df_long, x="Year", y="Value [€/kWh]", color="country", title=f"{selected_constant} for {len(dfs)} countries")
                fig.update_layout(width=800,
                                height=400,  
                                margin=dict(l=0, r=0, b=0),
                                autosize=True)
                fig.update_traces(marker=dict(colorbar=dict(tickfont=dict(size=14))))

                st.plotly_chart(fig)

                st.write(f"<em>{selected_statistic} for {country} from year: {str(year_from)} DataFrame</em>", unsafe_allow_html=True)
                st.write(merged_df)