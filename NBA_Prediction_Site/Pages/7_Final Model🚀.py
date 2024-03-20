import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import altair as alt

st.title("Final Model 🚀")

st.header("Model:")
st.subheader("Features 👀")
st.write("- Top 7️⃣ Features in LASSO Regression")

st.subheader("Algorithm 👨🏻‍💻")
st.write("- Random Forest Regressor 🌲🌲🌲")

st.subheader("Hyperparameters ⚙️")
st.write("- max_depth ⏬: 4")
st.write("- min_samples_leaf 🍂: 7")
st.write("- min_samples_split ✂️: 2")
st.write("- n_estimators 🌳: 10")
st.write("- random_state 🎲: 0")

df = pd.read_csv("C://Users/60102/Desktop/championship_win_share_predictions.csv", encoding="utf-8-sig", low_memory=False)

st.header("Model Results 📝")
# Combine Actual Value and Predicted Value into a single DataFrame
combined_df = pd.concat([df['Testing Data'], df['Actual Value'], df['Predicted Value']], axis=1)
combined_df = combined_df.melt('Testing Data', var_name='Variable', value_name='Value')

st.subheader("Scoring 🎯")
df_results = pd.read_csv("C://Users/60102/Desktop/ModelResults.csv", encoding="utf-8-sig", low_memory=False)

st.data_editor(df_results, width = 500)

st.subheader("Line Graph 📈")
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

st.write("The line graph above shows the predicted CWS value VS the actual CWS value after tuning the hyperparameters of the final model.")
