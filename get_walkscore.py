# Imports
import requests
import json
import pandas as pd
import csv
import config

# load excel .csv with long, lat points into pd dataframe
coordinate_df = pd.read_csv('grid.csv')

# convert pd dataframe into python dictionary, with coordinates as keys
coordinate_list = coordinate_df.values.tolist()
# print(coordinate_list)

walkscore_csv = []
points_w_error = []

# iterate through coordinate_list (list of lists)
# coordinate_list[i] = [lon, lat, walkscore]
for i in range(len(coordinate_list)): # range(len(coordinate_list)):
  try:
  # api call to walkscore using lon and lat parameters
    url = f"https://api.walkscore.com/score?format=json&lat={coordinate_list[i][1]}&lon={coordinate_list[i][0]}&wsapikey={config.api_key}"
    response = requests.get(url)
    # json_response  = json.loads(response.content['walkscore'])
    lat = coordinate_list[i][1]
    lon = coordinate_list[i][0]
    json_response = json.loads(response.content)
    # print(json_response['walkscore'])
    walkscore = json_response['walkscore']
    print((lon, lat, walkscore))
    # add to list that will be exported into .csv
    walkscore_csv.append([lon, lat, walkscore])
  # make exception that records all the points that give an error.
  except KeyError:
    print((coordinate_list[i][0], coordinate_list[i][1], "error"))
    walkscore_csv.append([coordinate_list[i][0], coordinate_list[i][1], "error"])
    points_w_error.append([coordinate_list[i][0], coordinate_list[i][1]])
print("Done! Check output .csvs for any errors")

# export list of points that return errors
with open('errors.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Longitude', 'Latitude', 'Walkscore'])
  for i in range(len(points_w_error)):
    writer.writerow([points_w_error[i][0], points_w_error[i][1]])

# export lon, lat, walkscore into csv for importing into arcgis
with open('walkscore_csv_export.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Longitude', 'Latitude', 'Walkscore'])
  for i in range(len(walkscore_csv)):
    writer.writerow([walkscore_csv[i][0], walkscore_csv[i][1], walkscore_csv[i][2]])


def junk():
# JUNK:
# for index, rows in coordinate_df.iterrows():
  # url = f"https://api.walkscore.com/score?format=json&lat={lat}&lon={lon}&wsapikey=7440f2082150c4593d7c8ba8ec092c62"
  # response = requests.get(url)
  # json_response  = json.loads(response.content['walkscore'])
  # print(coordinate_df.loc[])
  # convert df to list or dict? list it is

  # plan
  # iterate through dataframe using for index, col in dataframe
  # note: index is the row # and col is the name of the column
  # add walkscore data for each point

# coordinate_df.loc[0, 'Walkscore'] = 1
# print(coordinate_df)
# print(coordinate_dict)
# lon = -119.843813
# lat = 	34.413216
# test_url = f"https://api.walkscore.com/score?format=json&lat={lat}&lon={lon}&wsapikey=7440f2082150c4593d7c8ba8ec092c62"
# test_response = requests.get(test_url)
# test_json_response = json.loads(test_response.content)
# print(test_json_response['walkscore'])  # walkscore of 61
  print("hi")
