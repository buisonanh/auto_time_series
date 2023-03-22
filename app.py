import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Import profiling capabilities
from streamlit_pandas_profiling import st_profile_report

# ML libraries
from sklearn.linear_model import LinearRegression

with st.sidebar:
    st.image("image.png")
    st.title("Stock Price Visualize Tool")
    choice = st.radio("Menu", ["Upload", "Profiling", "Visualize", "Download"])
    st.info("You can upload your stock price history dataset and get the visualization of the data.")

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload your dataset")
    file = st.file_uploader("Upload your file here:")
    if file:
        df = pd.read_csv(file, index_col=None)
        df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    if st.button("Start Profiling"):
        profile_report = df.profile_report()
        st_profile_report(profile_report)

if choice == "Multiple Linear Regression":
    st.title("Linear Regression")
    if st.button("Start Predicting"):
        lrm = LinearRegression()

        g = df[['wheel-base', 'width', 'curb-weight', 'engine-size', 'horsepower', 'highway-mpg']]
        y_m = df['price']
        lrm.fit(g,y_m)

        y_m_predict = lrm.predict(g)
        y_m_predict[0:5]
        print(f'Ptrinh du doan gia bang cac bien la: y = {lrm.coef_[0]} wheel-base +  {lrm.coef_[1]} width +  {lrm.coef_[2]} curb-weight +  {lrm.coef_[3]} engine-size + {lrm.coef_[4]} horsepower + {lrm.coef_[5]} highway-mpg + {lrm.intercept_}')
if choice == "Download":
    st.title("Download the file")
    

