import streamlit as st
import pandas as pd
import requests

st.title("Hello, Joey!")
st.write("Welcome to your first Streamlit app!")

@st.cache_data()
def load_data():
    """returning Data Frame on Webpage
    :return: class_df
    :rtype: DataFrame 
    """
    data = {'courses':['Technology', 'Platforms', 'Infrastructure', 
                    'Project Work I',
                    'Governance'],
            'locations':['Lindholmen', 'Kuggen', 'Humanisten', 'Järntoget',
                        'Näsetbadet'],
            'coordinate': None}
    class_df = pd.DataFrame(data=data)
    return class_df

@st.cache_data()    
def update_table(df: pd.DataFrame,
                column: str,
                row: int,
                selected_value: str):
    """updates the data in cached df after input
    :param df: dataframe to update
    :type df: Geodf
    :param selcted_value: object
    :type selcted_value: str
    :return: updated df
    :rtype: df
    """
    df.loc[row, column] = selected_value
    return df

class_df = load_data()
st.write('Can you change these to the correct locations?')
df_placeholder = st.empty()
df_placeholder.dataframe(class_df)

#changing a course
courses_values = ["Select a course"] + list(class_df.courses.unique())

selected_course = st.selectbox("Select a course:",
                            options= courses_values,
                            index= 0,
                            key= "course_select")

if selected_course != "Select a course":
    loc_values = ["location or coordinate?"] + ['location','coordinate']

    poi_or_coordinate = st.selectbox("Select which column to change:",
                                    options= loc_values,
                                    index= 0,
                                    key= "type_select")
    # changing the location (POI)
    if poi_or_coordinate == 'location':
        # location_select‘
        selected_location = st.selectbox("Select a location:",
            options= ["Select a location"] + class_df['locations'].to_list(),
            index= 0,
            key= "loc_select")
        if selected_location != "Select a location":
            if st.button("Update value"):
                row_index = class_df[class_df['courses'] == selected_course].index[0]
                class_df = update_table(df= class_df,
                                        column= 'locations',
                                        row=row_index,
                                        selected_value=selected_location)
                st.write("DataFrame updated!")
                df_placeholder.dataframe(class_df)

    # changing a coordinate:
    elif poi_or_coordinate == 'coordinate':
        st.write('coordinate!')
