import requests

#launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P), if "import requests could not be resolved from source"

# ------- Indicators API IWB -----------
# Replace token: open iwb in browser, inspect, application tab, local storage, and you get an access token valid for 1h (do not use ID token).
# doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# Call "as of": use "https://iwb-dev.evooq.io/api/indicators/timeseries/global-financial-risk/summary?asOf=1654560000000".
# Time is in nanoseconds. Use "https://www.unixtimestamp.com/" (in milliseconds) and add three 0 to get milliseconds

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBLdlkwOHREak1kWlVCZ2gtSzZISSJ9.eyJodHRwczovL2V2b29xLmlvL25hbWUiOiJUaG9tYXMgQ2liaWxzIiwiaHR0cHM6Ly9ldm9vcS5pby9lbWFpbCI6InRob21hcy5jaWJpbHNAZXZvb3EuY2giLCJodHRwczovL2VkZ2VsYWIuY2gvb3JnYW5pemF0aW9uX2lkIjoiM2RkOWEzMWEtNzBmMy00NzQyLWJmMGUtMzI4YmExY2RmMjQ3IiwiaHR0cHM6Ly9ldm9vcS5pby91c2VyX3JvbGVzIjpbIm1pcC1pbmRpY2F0aXZlIiwibGNtLWJhc2ljIiwiYWMtY29uc3VtZXIiLCJpd2ItZnVsbCJdLCJodHRwczovL2V2b29xLmlvL3pvbmVpbmZvIjoiRXVyb3BlL1p1cmljaCIsImlzcyI6Imh0dHBzOi8vbG9naW4uZXZvb3EuaW8vIiwic3ViIjoiYXV0aDB8NWY2MDdmYjQ1OTFkY2UwMDcwM2VhNjFlIiwiYXVkIjpbImh0dHBzOi8vZXZvb3EuZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2V2b29xLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NTY4NzQxNjcsImV4cCI6MTY1Njk2MDU2NywiYXpwIjoiOWJUcDNjWjBpa0dyTG81RlcxT09mbWJudHk3TXdrYU0iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.PeLvUwrW6pnHDMoxBXRGVCbxA1zgc0QTL8E-aHVz9mn4NVXCVNI2YxpTm1yvPEQDNIjL9Dsqi1XkMuxOHZ2Klp8etANTi4g5jW3OKkCaBFd4gR2FuJR5mDL8OjP9P3oQvUMB6TxoLB7VydssONIGSSI8lib2qnYzJytUsdWtqRe6-iBk6bq_ta28aJI3Yf9ZWyYUgtsTI3VdqnEBbNXT_698wHXEvcl0mddueZ4IWXfzHZce90iv67BuRIOBXZWNAJAqwmxgQLmcZj2aQxaryk_wGhYxlfQLM-k1s_QVlAQWwSeFq37JteVBJf89iN_fyFU3EBvAIbAah5CcP6nTqQ"

#DO NOT PUSH TO GIT WITH TOKEN CLEAR

reqIWB = requests.get("https://iwb.evooq.io/api/indicators/timeseries/global-financial-risk/summary", headers={"Authorization": f"Bearer {token}"})

print(reqIWB.json())