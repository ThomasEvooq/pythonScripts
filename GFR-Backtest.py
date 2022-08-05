from ast import increment_lineno
from cProfile import label
from cmath import nan
from operator import index
import streamlit as st
import pandas as pd
import requests
import time 

# ------- VS Code Basic Debug -----------
# if "import requests could not be resolved from source":
# launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P)
# if "command 'python.setInterpreter' not found"
# Bottom left in purple/blue bar, click "restricted mode", trust workspace

# ------- Data Gathering --------------
# Use dedicated script getIndicatorsFiles.py to get csv files used
# Adapt script parameters to get real date as timestamp in csv
# Better to separate the script to avoid reload data everytime this is launched

# ------- Streamlit launch -----------
# launch: cmd -> go in directory -> streamlit run test.py
# stop: ctrl + C in cmd

# ------- Static data ----------------
twentyseventeenjanfirst = 1483228800000
twentyeighteenjanfirst = 1514764800000
twentynineteenjanfirst = 1546300800000
twentytwentyjanfirst = 1577836800000
twentytwentyonejanfirst = 1609459200000
twentytwentytwojanfirst = 1640995200000

# ------- Loading CSV Data ------------
SPXdf = pd.read_csv('SPX.csv')
SPXdf = SPXdf.set_index('TimeStamp')
# st.write(SPXdf) 

GFRdf = pd.read_csv('GFR.csv')
GFRdf = GFRdf.set_index('TimeStamp')
# st.write(GFRdf)
# st.line_chart(GFRdf)

# ------- Smoothing data -----------
# Joining data in single dataframe
globaldf = GFRdf.join(SPXdf, how = 'outer')
# st.write(globaldf)

# Filling NA data of weekend of SPX with previous value. We are left with 2 missing value from the start. I cheated by edditing the csv by hand for these values.
globaldf.fillna(method='ffill', inplace = True)
# st.write(globaldf)

# Convertine GFR in bool
boolGFR = globaldf['GFR'] == 'POSITIVE'
# st.write(boolGFR)

# Initializing the strategy value with same base as SPX
#cheating again to avoid 0 cases at start
strategy = [globaldf.iloc[0]['SPX']] 

iterator = 1 # Avoiding the weekend with identical values
maxIterator = len(globaldf)

while iterator < maxIterator:
    # If we are risk on
    if(boolGFR[iterator]):
        # We grow in same proportion as SPX
        growthRate = 1 + (globaldf.iloc[iterator]['SPX'] - globaldf.iloc[iterator-1]['SPX']) / globaldf.iloc[iterator]['SPX']
        strategy.append(strategy[iterator-1] * growthRate)
    
    # If we are risk off
    if(not boolGFR[iterator]):
        # We have a growth of 0
        strategy.append(strategy[iterator-1])
       
    iterator += 1

#Creating dataframe from list with same index as the others with the dates
Strategydf = pd.DataFrame(index=globaldf.index, data=strategy, columns={'Strategy'})

# Joining data in a single dataframe
fullDataFrame = pd.concat([globaldf['SPX'], Strategydf], axis = 1)

# Computing generated Alpha
fullDataFrame['Alpha'] = fullDataFrame['Strategy'] - fullDataFrame['SPX']


# Display everything
st.write("# Backtest GFR in Streamlit")
st.write("I built this webpage for two main reasons. First, I was curious to see a small backtest of the Global Financial Risk from the Investment Workbench, even a naive one. And secondly, I wanted to code a bit by myself again, and give a try to streamlit :smile: I downloaded GFR and S&P values from the IWB API and used it to plot the graphs below.")
st.markdown("The Strategy backtested here is quite simple:")
st.markdown(" - We start with with exactly the same as the S&P value.")
st.markdown(" - Then, if the GFR is positive and Risk-On :thumbsup:, we assume we get the same return as the S&P, positive or negative.")
st.markdown(" - If the GFR is negative and Risk-Off :thumbsdown:, we assume that we get 0 return, as if we were full cash, and our strategy does not move.")
st.write("The strategy below is run on a 6y period. Please do not pay attention to the graph legend, for some reason, streamlit shows the date of everyday, I did not fix that yet.")

st.write("## S&P, Risk-based Strategy and Alpha")
st.line_chart(fullDataFrame)

st.write("## Alpha as difference between S&P and Strategy")
st.area_chart(fullDataFrame['Alpha'])

st.write("## Strategy Performance")
st.line_chart(Strategydf)

st.write("## S&P")
st.line_chart(SPXdf)

st.write("## GFR over time")
st.line_chart(GFRdf)