import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

st.title("Data Cleaning 🧹")
st.write("Datasets can be dirty sometimes 💩, so let's clean it!")
df = pd.read_csv("C://Users/60102/Desktop/champ_data_edit.csv", encoding="utf-8-sig", low_memory=False)
df = df[df['season'] <= 2022]

# Calculate null values count for each season
nullVal_season = []
nullVal_count = []

for season in df['season'].unique(): 
    nullVal_season.append(season)
    x = sum((df[df['season'] == season].isnull().sum(axis=1)))
    nullVal_count.append(x)

# Create a DataFrame from the calculated values
data = {'Season': nullVal_season, 'Sum of Null Values': nullVal_count}
df_nullCount = pd.DataFrame(data)

st.header('Sum of Null Values in Every NBA Season')

# Display the line graph
st.line_chart(data=data, x= "Season", y= "Sum of Null Values", color=None, width=0, height=0, use_container_width=True)

st.write("The graph shows fewer missing values until about 1980 when they disappear, likely because advanced stats weren't tracked and the 3-point shot wasn't recorded before then. Therefore the NBA dataset is filtered to include only data from the 1980 NBA season onwards. However, there's a significant increase in missing values around 2000 NBA Season.")

# Assuming nullprepost is a dictionary containing the count of null values for 'Pre' and 'Post' columns
nullprepost = {'Pre': df['Pre'].isnull().sum(), 'Post': df['Post'].isnull().sum()}

# Create a Streamlit app
st.header('Count of Null Values in Pre and Post Columns')

# Draw the bar chart
st.bar_chart(data=nullprepost, use_container_width=True)

st.write("After removing the 'Pre' and 'Post' columns, the dataset is finally cleaned!")
