import streamlit as st

st.title("Hyperparameter Tuning 🛠️")
st.write("Hyperparameters are basically settings that control the learning process itself like how fast a model learns, how complex it can be, or how flexible it is. Fix it Felix! 👨‍🔧")

st.header("HyperOpt-Sklearn 🤓")
st.write("Hyperopt-sklearn combines two tools: Hyperopt for finding the best hyperparameters and scikit-learn for machine learning algorithms. It helps automatically tune the parameters of scikit-learn models for better performance!")


st.header("Random Forest Regressor's Hyperparameters ⚙️")
st.subheader("max_depth ⏬: 4")
st.write("It decides how deep each tree in the forest can grow. Deeper trees can capture more complex patterns but may overfit.")

st.subheader("min_samples_leaf 🍂: 7")
st.write("It sets the minimum number of samples allowed in a leaf node. It helps prevent overfitting by stopping the tree from splitting too much")

st.subheader("min_samples_split ✂️: 2")
st.write("It sets the minimum number of samples required to split an internal node. It helps prevent overfitting by controlling when nodes can split.")

st.subheader("n_estimators 🌳: 10")
st.write("It determines how many trees are built in the forest. More trees can improve performance but also increase computation time.")

st.subheader("random_state 🎲: 0")
st.write("It ensures that the random splits in the trees are reproducible. Setting this value ensures consistent results each time you run the algorithm.")