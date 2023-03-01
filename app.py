import streamlit as st
import pandas as pd
import os 

# Import profiling capabilities
import pandas_profiling



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
    pass


if choice == "Model":
    pass


if choice == "Download":
    pass
    

