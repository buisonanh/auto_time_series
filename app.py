import streamlit as st
import pandas as pd
import os 

# Import profiling capabilities
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

# ML libraries
from pycaret.classification import setup, compare_models, pull, save_model


with st.sidebar:
    st.image("image.jpg")
    st.title("Time-series Prediction Tool")
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
    st.title("Machine Learning Model")
    target = st.selectbox("Select Your Target", df.columns)
    setup(df, target=target, silent=True)
    setup_df = pull()
    st.info("This is the ML experiment settings")
    st.dataframe(setup_df)
    best_model = compare_models()
    compare_df = pull()
    st.info("This is the ML Model")
    st.dataframe(compare_df)
    best_model

if choice == "Download":
    pass
    

