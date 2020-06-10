import requests
import pandas as pd

#API url for raw-data from covid19india.org
url = "https://api.covid19india.org/data.json"
#Requesting the api to provide data
response = requests.get(url)
#Printing the response code --> if 200 then everything went fine
if response.status_code==200:
  print("Request successful")
#Converting json to dataframe
data = response.json()
df_raw_data = pd.DataFrame(data["raw_data"])
#print(df_raw_data)
#Dumping dataframe to csv
df_raw_data.to_csv("data.csv")
