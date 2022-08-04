import streamlit as st
import pandas as pd

# launch: cmd -> go in directory -> streamlit run test.py
# stop: ctrl + C in cmd

st.write("# Hello world")

df = pd.read_csv('example.csv')
st.write(df)
st.line_chart(df)