import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import altair as alt

st.title("Algorithm 👨🏻‍💻")
st.header("Random Forest Regressor 🌲🌲🌲")
st.write("Random Forest Regressor is a machine learning algorithm that combines predictions from many decision trees to make accurate forecasts for numerical values.")
st.write("Imagine you are trying to guess how much money your friend, Nicholas has. So you ask all of his friends (who knows his financial situation) to guess. Then you average their guesses to get a prediction, which should be 0! 😭😭😭")

st.subheader("Line Graph")

df = pd.read_csv("C://Users/60102/Desktop/RFR_predictions.csv", encoding="utf-8-sig", low_memory=False)

# Combine Actual Value and Predicted Value into a single DataFrame
combined_df = pd.concat([df['Testing Data'], df['Actual Value'], df['Predicted Value']], axis=1)
combined_df = combined_df.melt('Testing Data', var_name='Variable', value_name='Value')

# Plotting using Altair
chart = alt.Chart(combined_df).mark_line().encode(
    x='Testing Data',
    y='Value',
    color=alt.Color('Variable', scale=alt.Scale(domain=['Actual Value', 'Predicted Value'], range=['lightblue', 'orange'])),
    strokeDash=alt.condition(
        alt.datum.Variable == 'Predicted Value',
        alt.value([3, 3]),
        alt.value([0])
    )
).properties(
    width=900,  # Adjust the width as needed
    height=400   # Adjust the height as needed
).interactive()

# Display the chart
st.altair_chart(chart)

st.write("The line graph above shows the predicted CWS value VS the actual CWS value using Random Forest Regressor before hyperparameter tuning.")