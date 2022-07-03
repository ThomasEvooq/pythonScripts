import requests

#launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P)

# ------- Indicators API IWB -----------
# Replace token: open iwb in browser, inspect, application tab, local storage, and you get an access token valid for 1h (do not use ID token).
# doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# Call "as of": use "https://iwb-dev.evooq.io/api/indicators/timeseries/global-financial-risk/summary?asOf=1654560000000".
# Time is in nanoseconds. Use "https://www.unixtimestamp.com/" (in milliseconds) and add three 0 to get milliseconds

token = ""

#DO NOT PUSH TO GIT WITH TOKEN CLEAR

reqIWB = requests.get("https://iwb.evooq.io/api/indicators/timeseries/global-financial-risk/summary", headers={"Authorization": f"Bearer {token}"})

print(reqIWB.json())