import streamlit as st
import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt

# Import profiling capabilities
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

# ML libraries
from sklearn.linear_model import LinearRegression


with st.sidebar:
    st.image("image.jpg")
    st.title("Stock Prediction Tool")
    choice = st.radio("Menu", ["Upload", "Profiling", "Model", "Download"])
    st.info("This a tool created by Son Anh where you can upload your dataset and \
            you can get the predictions based on a time-series model, which will be able to download later on")
    
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload your data for modeling")
    file = st.file_uploader("Upload your file here:")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)


if choice == "Model":
    X_train = df['feature'].values.reshape(-1, 1)
    y_train = df['target'].values.reshape(-1, 1)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    new_feature_value = 10
    predicted_price = regressor.predict(np.array(new_feature_value).reshape(-1, 1))
    st.dataframe(predicted_price)


if choice == "Download":
    pass
    

