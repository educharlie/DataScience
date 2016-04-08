import requests
import json
worldbank_url = "http://api.worldbank.org/countries/all/indicators/SP.RUR.TOTL.ZS?date=2000:2015&format=json"
r = requests.get(worldbank_url)
jsondata = json.loads(r.text)
print(jsondata[1])
print(r.status_code)