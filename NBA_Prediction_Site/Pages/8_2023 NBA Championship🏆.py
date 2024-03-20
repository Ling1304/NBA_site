import streamlit as st
import pandas as pd

st.title("2023 NBA Championship Forecast Comparison 🏆")

st.header("Top 8️⃣ 2023 NBA Championship Teams")
st.subheader("Actual vs Predicted")

df = pd.read_csv("C://Users/60102/Desktop/2023_pred.csv", encoding="utf-8-sig", low_memory=False)

st.data_editor(df, width = 500)

st.write("In the 2023 NBA playoffs, the Milwaukee Bucks, as the top seed, faced an unexpected defeat against the Miami Heat in the first round, losing 4-1. This marked the sixth time in history that a No.1 seed failed to advance to the second round. The Bucks' defeat was partly due to their best player playing through an injury. On the other hand, the Miami Heat made history by becoming the second team in NBA history to reach the NBA Finals after entering the playoffs as an eighth seed.")