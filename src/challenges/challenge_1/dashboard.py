import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests
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
                
                1. Download the data from 'https://github.com/teofizzy/dte_datathon/blob/teo/src/data/challenge_1_cleaned.csv'
                2. There is an option to select your year of choice, variable of choice.
                3. There is an option to select one variable or more. If you select one variable, you shall see the its change over time
                4. You can select any two variables of your choice to see their relationship
                
                ---
                
                ''')
    


upload_file = st.file_uploader("Upload file", ['csv'])

# Load the data directly from the URL
def load_data():
    df = pd.read_csv(upload_file)
    return df

df = load_data()

df = df[['time', 'agricultural_land_%_of_land_area', 'agriculture_forestry_and_fishing_value_added_annual_%_growth', 
         'access_to_electricity_urban_%_of_urban_population', 'adults_ages_15-49_newly_infected_with_hiv',
         'urban_population_%_of_total_population', 'urban_population_growth_annual_%', 'urban_population',
         'rural_population', 'rural_population_%_of_total_population', 'rural_population_growth_annual_%',
         'population_growth_annual_%', 'gdp_growth_annual_%', 'gdp_current_US$']]

df["date"] = pd.to_datetime(df["time"])

# Getting the min and max date 
startDate = pd.to_datetime(df["date"]).min()
endDate = pd.to_datetime(df["date"]).max()

# select a year
st.header("Pick a year and pick your variables of interest for that year")
st.info("Disclaimer :exclamation: There are variables that are proportions (have %) and there are variables that are figures,\
        for a better experience, kindly don't pick mix the two. Choose variables of one type")
selected_year = st.selectbox("Select Year of Interest", df['date'].dt.year.unique())

year_filtered_df = df[df['date'].dt.year == selected_year]
    
# Select variables for the bar chart
selected_bar_chart_variables = st.multiselect("Select Variables for Bar Chart", df.columns, key='bar_chart')

# Display data for the selected year and variables
if selected_year and selected_bar_chart_variables:
    st.info(f"Bar Chart Data for the Year {selected_year} and Selected Variables")
    year_filtered_df = df[df['date'].dt.year == selected_year]

    # Create a bar chart with each selected variable having its own bar
    fig = px.bar(
        year_filtered_df.melt(id_vars=['date'], value_vars=selected_bar_chart_variables),
        x='date',
        y='value',
        color='variable',
        title=f'Bar Chart for Year {selected_year}',
        barmode='group',  # This sets bars side by side
    )
    st.plotly_chart(fig)
    

# select variable
st.header("Pick variable(s) of interest to see their change over time")
selected_variables_ts = st.multiselect("Select Variable(s) of Interest (a maximum of 2 variables allowed)", df.columns)

def plot_time_series(df, x_col, y_col1, y_col2=None):
    st.write(f"Selected x column: {x_col}")

    if not y_col1:
        st.error("Please select at least one y column.")
        return
    
    if y_col1 == 'date' or (y_col2 and y_col2 == 'date') or y_col1 == 'time' or y_col2 == 'date':
        st.error("Please select another column in place of 'date' ")
        return 

    st.write(f"Selected y column 1: {y_col1}")
    if y_col2:
        st.write(f"Selected y column 2: {y_col2}")

    # Create a line plot for each selected y column
    fig1 = px.line(df, x=x_col, y=y_col1, title=f"Time Series Plot for {y_col1}")
    if y_col2:
        fig2 = px.line(df, x=x_col, y=y_col2, title=f"Time Series Plot for {y_col2}")

        # Create two columns for the two plots
        col1, col2 = st.columns(2)

        # Display the plots in separate columns
        col1.plotly_chart(fig1)
        col2.plotly_chart(fig2)
    else:
        st.plotly_chart(fig1)

if selected_variables_ts:
    plot_time_series(df, x_col='date', y_col1=selected_variables_ts[0], y_col2=selected_variables_ts[1] if len(selected_variables_ts) > 1 else None)
    
    
# Function to calculate and print correlation for two variables
def calculate_and_print_correlation(df, var1, var2):
    correlation_coefficient = df[var1].corr(df[var2])
    st.write(f"Correlation coefficient between {var1} and {var2}: {correlation_coefficient:.3f}")
    
    if correlation_coefficient > 0.5 and correlation_coefficient < 0.75:
        st.write(f"There is a moderately strong positive correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a moderately strong increase in {var2}.")

    elif correlation_coefficient > 0.75 and correlation_coefficient < 1.0:
        st.write(f"There is a very strong positive correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a very strong increase in {var2}.")

    elif correlation_coefficient > 0 and correlation_coefficient < 0.5:
        st.write(f"There is a weak positive correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a weak but positive increase in {var2}.")

    elif correlation_coefficient < 0 and correlation_coefficient > -0.5:
        st.write(f"There is a weak negative correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a weak decrease in {var2}.")

    elif correlation_coefficient < -0.5 and correlation_coefficient > -0.75:
        st.write(f"There is a moderately strong negative correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a moderately strong decrease in {var2}.")

    elif correlation_coefficient > -1 and correlation_coefficient < -0.75:
        st.write(f"There is a very strong negative correlation between {var1} and {var2}.")
        st.write(f"This means that an increase in {var1} is associated with a very strong decrease in {var2}.")

# Calculate and print correlations for two selected variables
if len(selected_variables_ts) == 2:
    calculate_and_print_correlation(df, selected_variables_ts[0], selected_variables_ts[1])



# if selected_variables:
#     st.write(year_filtered_df[selected_variables])
    
    
# if st.button("Perform Correlation Test"):
#     correlation_matrix = year_filtered_df[selected_variables].corr()
#     st.write("Correlation Matrix:")
#     st.write(correlation_matrix)
    
# if st.button("Perform Granger Causality Test"):