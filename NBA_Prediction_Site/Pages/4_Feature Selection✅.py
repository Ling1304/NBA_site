import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import altair as alt

st.title("Feature Selection ✅")
st.write("Some features are not useful 🗑️, so we only select features that are useful!")

st.header('LASSO Regression')
st.write("LASSO Regression works by shrinking the less important features towards zero, leaving only the most important features in the final prediction.")
st.subheader('Top 15 Most Important Features')

df = pd.read_csv("C://Users/60102/Desktop/df_lasso_features.csv", encoding="utf-8-sig", low_memory=False)

chart = (
    alt.Chart(df, width=800, height=600)  # Adjust width and height as needed
    .mark_bar()
    .encode(
        x=alt.X("Lasso_Coef", title="Importance (Lasso Co-efficient)"),
        y=alt.Y("Lasso_Features", type="nominal", title="Features", sort=alt.EncodingSortField(field="Lasso_Coef", order='descending'))
    )
)

st.altair_chart(chart, use_container_width=True)