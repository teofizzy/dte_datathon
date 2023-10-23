# dte_datathon
This is a repository to serve as the team's remote repo for the dte datathon

Below is the project structure:
# src

* [challenges/](./src/challenges)
  * [challenge_1/](./src/challenges/challenge_1)
    * [about.py](./src/challenges/challenge_1/about.py)
    * [dashboard.py](./src/challenges/challenge_1/dashboard.py)
    * [t_index.ipynb](./src/challenges/challenge_1/t_index.ipynb)
  * [challenge_2/](./src/challenges/challenge_2)
    * [dte_datathon_data_report.pdf](./src/challenges/challenge_2/dte_datathon_data_report.pdf)
    * [etl_system.py](./src/challenges/challenge_2/etl_system.py)
    * [index_2.ipynb](./src/challenges/challenge_2/index_2.ipynb)
    * [readme.md](./src/challenges/challenge_2/readme.md)
    * [s3_cli.sh](./src/challenges/challenge_2/s3_cli.sh)
* [reports/](./src/reports)


## Challenge 1 Summary:
The first challenge was focused on urbanization in Kenya.
The study sought to find the patterns and trends associated with urbanization in Kenya.
The data was obtained from worldbank and the variables that were used in the study include:
* time ~ the year of the data point.
* agricultural_land_%_of_land_area~ the proportion of land that is allocated for agriculture in Kenya.
* agriculture_forestry_and_fishing_value_added_annual_%_growth ~ the value added % change from agriculture, forestry and fishing.
* access_to_electricity_urban_%_of_urban_population ~ proportion of the urban population that have access to electricity as a percentage.
* adults_ages_15-49_newly_infected_with_hiv ~ newly reported cases of hiv
* urban_population_%_of_total_population ~ proportion of the population that live in urban areas
* urban_population_growth_annual_% ~ change in urban population from the previous year as a percentage.
* urban_population ~ urban population raw figure
* rural_population ~ rural population raw figure
* rural_population_%_of_total_population ~ proportion of the population that live in rural areas as a percentage.
* rural_population_growth_annual_% ~ % change in rural population from the previous year.
* population_growth_annual_% ~ % change in the total population from the previous year.
* gdp_growth_annual_% ~ % change in gdp from the previous year.
* gdp_current_US$~ the current value of the country's gdp in us dollars.

### The conclusions from the study were as follows:
* The association between urban population growth % and agricultural land % of land area exhibits a behavior such that if urban population growth % increases the proportion of land in the country that is allocated for agriculture reduces. But this is not very bad because the value added from agriculture and fishing, though weak is positive.
* An increase in urban population growth % is associated with an increase in adult ages 15-49 newly infected with hiv. This suggests that as urbanization increases, the new cases of hiv also increase.
* We also found that an increase in urban population growth % is associated with an decrease in unemployment rate. This suggests that amidst the rising annual growth in urbanization, unemployment rate decreases over the years. Urbanization creates jobs for the population.
* The impact of urban population growth % is influences agricultural land % of land area for at least 2 years.
* The impact of urban population growth % influences unemployment after 2 years as shown by the granger causality test. For example, the increase in urban population growth % in 2021 is felt by unemployment rate in 2023.
* The impact of urban population growth % influences gdp current after 1 year as shown by the granger causality test.
*  Over the years `agricultural_land_%_of_land_area`, `access_to_electricity_urban_%_of_urban_population`, `urban_population_%_of_total_population`, `urban_population`, `rural_population`, `rural_population_%_of_total_population` `gdp_current_US$` and `access_to_electricity_%_of_population` show an increase in value.
* `agriculture_forestry_and_fishing_value_added_annual_%_growth` fluctuates over the years.
* `urban_population_growth_annual_%` and `rural_population_growth_annual_%` show a declining trend. This makes sense because even `population_growth_annual_%` exhibits a declining trend. The population itself is growing but the annual change is declining.

### The recommendations from the study include:
The main stakeholder is the government of Kenya. The study recommends the following to the stakeholder:
1. The government should invest in data collection and analysis to monitor urbanization trends and their impacts. Data-driven decision-making will enable the government to adapt policies and strategies as needed.
2. As urbanization is associated with a decrease in unemployment rates, the government should continue to invest in policies and programs that promote job creation in urban areas. This could include initiatives to support entrepreneurship, vocational training, and attracting industries that can provide employment opportunities.
3. To address the increase in adult ages 15-49 newly infected with HIV associated with urbanization, the government should prioritize HIV prevention and healthcare services in urban areas. Public awareness campaigns, access to testing, and healthcare infrastructure should be strengthened to curb the spread of HIV.
4. Given the negative association between urban population growth and agricultural land as a percentage of land area, the government should focus on urban planning that optimizes land use. Encourage sustainable urban development practices and consider allocating land for agriculture outside urban areas to ensure food security.

### Challenges:
The study encountered the following challenges:
1. Inadequate data. There is not much data on the kenyan government that has been made publicly available. This meant that we did not have enough data points to conduct a thorough study. Regional data such as county data is even harder to find. If more data was available or even if the data was monthly or quarterly the study would have had more data points.
2. The quality of the government records is not very good.
