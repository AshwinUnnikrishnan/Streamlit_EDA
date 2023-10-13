from operator import index
import streamlit as st
#import plotly.express as px
from pycaret.classification import setup, compare_models, pull, save_model, load_model
from ydata_profiling import ProfileReport

import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 




with st.sidebar:
    st.image('img/side.jpeg')
    st.title('AutoStreamML')
    choice = st.radio("Navigation", ["Upload", "Profiling", "Modelling", "Download"])
    st.info("This application allows you to build an automted ML pipeline using streamlit, pandas profiling and PyCaret.")

if os.path.exists("sourcedata.csv") and choice == "Upload":
    st.session_state.df = pd.read_csv("sourcedata.csv", index_col=None)



if choice == "Upload":
    st.title("Upload your data for modelling")
    file = st.file_uploader("Upload your dataset")
    if file:
        st.session_state.df = pd.read_csv(file, index_col=None)
        st.dataframe(st.session_state.df)
        if st.button("Save"):
            st.session_state.df.to_csv("sourcedata.csv", index=None)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    selected_columns = st.multiselect("Select columns to drop", st.session_state.df.columns)
    st.dataframe(st.session_state.df)
    # Add a button to drop selected columns
    if st.button("Drop Columns"):
        if selected_columns:
            st.session_state.df.drop(columns=selected_columns, inplace=True)
            st.dataframe(st.session_state.df)
    if st.button("Save"):
        st.session_state.df.to_csv("sourcedata.csv", index=None)
    if st.button("Perform EDA"):
    # Add code to remove timestamps and then do the profile report
        profile_df = ProfileReport(st.session_state.df, title="EDA")
        st_profile_report(profile_df)

if choice == "Modelling":
    columns_without_missing_values = [col for col in st.session_state.df.columns if st.session_state.df[col].count() == len(st.session_state.df)]

    target = st.selectbox("Select Your Target", columns_without_missing_values)
    if st.button('Run Modelling'): 
        # Mention to user if the missing value is present instead of throwing error
        setup(st.session_state.df, target=target)
        setup_df = pull()
        st.info("This is the ML Experiment Settings")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, 'best_model')

if choice == "Download":
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download the file", f, "best_model.pkl")