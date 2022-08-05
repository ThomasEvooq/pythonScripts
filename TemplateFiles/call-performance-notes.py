import requests

#launch ">python: select interpreter" if needed in the "Command Palette" (ctrl+shit+P)

# ------- Indicators API IWB -----------
# Replace token: open iwb in browser, inspect, application tab, local storage, and you get an access token valid for 1h (do not use ID token).
# doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# Call "as of": use "https://iwb-dev.evooq.io/api/indicators/timeseries/global-financial-risk/summary?asOf=1654560000000".
# Time is in nanoseconds. Use "https://www.unixtimestamp.com/" (in milliseconds) and add three 0 to get milliseconds
token = ""

# DO NOT PUSH TO GIT WITH CLEAR TOKEN

call request: to  https://iwb.evooq.io/api/indicators/timeseries/raw/performance

à mettre dans le body de la requête:

[
	{
		"symbol": 	"SPX Index",
		"weights": [
			{
				"value": 0.25,
				"startDate": 1591048800000
			}
		]
	},
	{
		"symbol": 	"NDDUUS Index",
		"weights": [
			{
				"value": 0.25,
				"startDate": 1591048800000
			}
		]
	},
	{
		"symbol": 	"MSDEE15N Index",
		"weights": [
			{
				"value": 0.25,
				"startDate": 1591048800000
			}
		]
	},
	{
		"symbol": 	"M7JP Index",
		"weights": [
			{
				"value": 0.25,
				"startDate": 1591048800000
			}
		]
	}
]