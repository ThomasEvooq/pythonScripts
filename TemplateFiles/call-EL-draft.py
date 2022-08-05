import requests

# DO NOT PUSH TO GIT WITH API KEY IN CLEAR
APIKeyEL = ""
reqEL = requests.get("https://api.edgelab.ch/recco/v2/risk-measures/volatility/granularities/positions", headers={"apikey": APIKeyEL}")

print(reqIWB.json())