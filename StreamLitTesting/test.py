# import streamlit as st
# import pandas as pd
import requests
import time 

# ------- VS Code Basic Debug -----------
# if "import requests could not be resolved from source":
# launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P)
# if "command 'python.setInterpreter' not found"
# Bottom left in purple/blue bar, click "restricted mode", trust workspace

# ------- Indicators API IWB -----------
# Replace token: open iwb in browser, inspect, application tab, local storage, and you get an access token valid for 1h (do not use ID token). Use the one from login.evooq.io, not the one from test
# Check token validity: print(reqIWB.status_code) - if 401, token is invalid
# doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# Call "as of": use "https://iwb-dev.evooq.io/api/indicators/timeseries/global-financial-risk/summary?asOf=1654560000000".
# Time is in nanoseconds. Use "https://www.unixtimestamp.com/" (in milliseconds) and add three 0 to get nanoseconds

# ------- Streamlit launch -----------
# launch: cmd -> go in directory -> streamlit run test.py
# stop: ctrl + C in cmd



token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBLdlkwOHREak1kWlVCZ2gtSzZISSJ9.eyJodHRwczovL2V2b29xLmlvL25hbWUiOiJUaG9tYXMgQ2liaWxzIiwiaHR0cHM6Ly9ldm9vcS5pby9lbWFpbCI6InRob21hcy5jaWJpbHNAZXZvb3EuY2giLCJodHRwczovL2VkZ2VsYWIuY2gvb3JnYW5pemF0aW9uX2lkIjoiM2RkOWEzMWEtNzBmMy00NzQyLWJmMGUtMzI4YmExY2RmMjQ3IiwiaHR0cHM6Ly9ldm9vcS5pby91c2VyX3JvbGVzIjpbIm1pcC1pbmRpY2F0aXZlIiwibGNtLWJhc2ljIiwiYWMtY29uc3VtZXIiLCJpd2ItZnVsbCJdLCJodHRwczovL2V2b29xLmlvL3pvbmVpbmZvIjoiRXVyb3BlL1p1cmljaCIsImlzcyI6Imh0dHBzOi8vbG9naW4uZXZvb3EuaW8vIiwic3ViIjoiYXV0aDB8NWY2MDdmYjQ1OTFkY2UwMDcwM2VhNjFlIiwiYXVkIjpbImh0dHBzOi8vZXZvb3EuZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2V2b29xLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NTk1OTc1OTIsImV4cCI6MTY1OTY4Mzk5MiwiYXpwIjoiOWJUcDNjWjBpa0dyTG81RlcxT09mbWJudHk3TXdrYU0iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.Hbk6H0XZQya8Qe8igBnK63qxeEwXY-h3Uo-EmcByxDhwRJ4zYETvOQjFNVg6muWfdcTcdW0bk9MQbCOqkJX21-bNzSKc0Ikt1hE3RYjKH-QNWKyw_Byq_2hld90fXuHH9l-_809D2-g5Mz3nti7uayMKDvqmM5KWZ2UUQ5c97Vu2U_xC4VtBl-FaHGGvYX8aDUF7Fb3YE5tClGZcfs0lYEOK6jcLeEGLf_WHeijDOnfZu29EtIfJx6kwKtbLL9AkxMQiVbW_BsWaGUbc8qL6mMtlcLNoOq3ItJOtJHUcP5ZM-FROR8sx5uDNHBhQ-okoEqOEHy0f8Qw6KwWkNtwswA"


#DO NOT PUSH TO GIT WITH TOKEN CLEAR
# https://iwb.evooq.io/api/indicators/timeseries/spxt/summary



#print(reqIWB.json())


currentTime = 1659484800000 #time.time_ns() 
nanoSecondsInDay = 86400000 
nanoSecondsInYear = 31556926000
yearInterval = 5

dataStampList = []
GFRList = []

# starting iterator years ago
iterator = currentTime - (yearInterval*nanoSecondsInYear)

while iterator < currentTime:
    dataStampList.append(iterator)
    baseRequestURL = "https://iwb.evooq.io/api/indicators/timeseries/global-financial-risk/summary?asOf="
    timeStringRequestURL = str(iterator)
    fullRequestURL = baseRequestURL + timeStringRequestURL
    # print(fullRequestURL)
    reqIWB = requests.get(fullRequestURL, headers={"Authorization": f"Bearer {token}"})
    #print(reqIWB.json())
    GFRList.append(reqIWB.json()['interpretation']['outlook'])
    iterator += nanoSecondsInDay


# st.write("# Testing Streamlit")

# df = pd.read_csv('example.csv')
# st.write(reqIWB.json())
# st.line_chart(df)

