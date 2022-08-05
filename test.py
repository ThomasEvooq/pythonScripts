import streamlit as st
import pandas as pd
import requests
import time 

# ------- VS Code Basic Debug -----------
# if "import requests could not be resolved from source":
# launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P)
# if "command 'python.setInterpreter' not found"
# Bottom left in purple/blue bar, click "restricted mode", trust workspace

# ------- Streamlit launch -----------
# launch: cmd -> go in directory -> streamlit run test.py
# stop: ctrl + C in cmd

st.write("# Testing Streamlit")

df = pd.read_csv('SPX.csv')
df = df.set_index('TimeStamp')
st.write(df)
st.line_chart(df)

