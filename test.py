import requests
import json
import pandas as pd
import csv

url = f"https://api.walkscore.com/score?format=json&lat=34.406985&lon=-119.889848&wsapikey=7440f2082150c4593d7c8ba8ec092c62"
response = requests.get(url)
json_response  = json.loads(response.content)
print(json_response)
# walkscore = json_response['walkscore']
  # add to list that will be exported into .csv
# print(walkscore)
