# Challenge 2 Overview:
This is the second of four phases required by the participants as stipulated by the dte datathon requiremnts. The challenge focuses on clinical trials from various parts of the world. The data, taken from [the clinical trials database](https://clinicaltrials.gov/) includes information about clinical research studies that are happening now, will happen soon, or happened in the past. It includes studies that take place in all 50 states and over 200 countries. The data for this study include clinical studies involving Cancer, malaria, Covid 19, HIV, Heart Conditions, and pneumonia which are some of the leading causes of death in Kenya.

![imageurl](https://t3.ftcdn.net/jpg/06/19/70/44/240_F_619704440_CUxs2uctpsOpjcshPyzCAGtqQLKOXiQ9.jpg)

## Project structure:
# challenge_2
* [dte_datathon_data_report.pdf](./challenge_2/dte_datathon_data_report.pdf)
* [etl_system.py](./challenge_2/etl_system.py)
* [index_2.ipynb](./challenge_2/index_2.ipynb) - data analysis file
* [readme.md](./challenge_2/readme.md)
* [s3_cli.sh](./challenge_2/s3_cli.sh) - aws client


## 1. Objective:
This study shall focus on two of the diseases named above, these are heart conditions. The objective of this study is to analyze the data with an aim of finding trends, patterns and insights that can be found within the data and communicate the findings of the study.

## 2. Data Collection and Ingestion:
Data of the clinical trials was downloaded from the provisions made by the dte team and stored in a centralized repository.

## 3. ETL System:
This was raw data and it might need preprocessing before any insights can be derived from it. The study will implement data processing and transformation pipelines that clean, format, and aggregate the data. The cleaned data will now be ready for analysis.

## 4. Data Lake:
The study shall use a centralised repo to store the data.

## 5. Analytics:
We will apply appropriate analytics techniques that will allow us uncover patterns, trends and insights from the data that we shall use.

## 6. Reporting:
The insights gained from our data analysis will be translated into actionable reports that allow effective communication of these insights.
