import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import about


st.set_page_config(page_title="Urbanization trends in Kenya", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("	:chart_with_upwards_trend: Urbanization in Kenya EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

with st.sidebar:
    about.main()
    st.markdown('''
                ---
                ## How to use
                
                1. There is an option to select your year of choice, variable of choice.
                2. There is an option to select one variable or more. If you select one variable, you shall see the its change over time
                3. You can select any two variables of your choice to see their relationship
                
                ---
                
                ''')
    
filepath = "src/data/challenge_1_cleaned.csv"

file = st.file_uploader(":file_folder: Upload a file",type=(["csv"]))

df = pd.read_csv(filepath)

if df:

    col1, col2 = st.columns((2))
    df["date"] = pd.to_datetime(df["time"])

    # Getting the min and max date 
    startDate = pd.to_datetime(df["date"]).min()
    endDate = pd.to_datetime(df["date"]).max()

    selected_year = st.selectbox("Select Year of Interest", df['date'].dt.year.unique())

    year_filtered_df = df[df['date'].dt.year == selected_year]
    
else:
    st.info("Please upload")