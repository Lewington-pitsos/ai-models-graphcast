import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

def get_forcast(openmeteo, params):
	url = "https://api.open-meteo.com/v1/forecast"

	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s"),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature_2m"] = hourly_temperature_2m

	hourly_dataframe = pd.DataFrame(data = hourly_data)
	return hourly_dataframe

def get_reanalysis(openmeteo, params):
	url = "https://archive-api.open-meteo.com/v1/archive"
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s"),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature_2m"] = hourly_temperature_2m

	hourly_dataframe = pd.DataFrame(data = hourly_data)

	return hourly_dataframe 

def get_om_data(params):
	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('cruft/.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	fo =  get_forcast(openmeteo, params)
	print('downloaded forcast')
	re = get_reanalysis(openmeteo, params)
	print('downloaded reanalysis')
	df = pd.merge(re, fo, on='date', how='outer', suffixes=['_reanalysis', '_forcast'])

	return df

start_date = '2023-12-22'
end_date = '2024-02-07'
param_name = f'{start_date}-{end_date}'

params = {
	# grid around melbourne
	"latitude": [-38.5 , -38.5 , -38.5 , -38.5 , -38.5 , -38.5 , -38.5 , -38.25,
       -38.25, -38.25, -38.25, -38.25, -38.25, -38.25, -38.  , -38.  ,
       -38.  , -38.  , -38.  , -38.  , -38.  , -37.75, -37.75, -37.75,
       -37.75, -37.75, -37.75, -37.75, -37.5 , -37.5 , -37.5 , -37.5 ,
       -37.5 , -37.5 , -37.5 , -37.25, -37.25, -37.25, -37.25, -37.25,
       -37.25, -37.25, -37.  , -37.  , -37.  , -37.  , -37.  , -37.  ,
       -37.  ],
	"longitude": [144.25, 144.5 , 144.75, 145.  , 145.25, 145.5 , 145.75, 144.25,
       144.5 , 144.75, 145.  , 145.25, 145.5 , 145.75, 144.25, 144.5 ,
       144.75, 145.  , 145.25, 145.5 , 145.75, 144.25, 144.5 , 144.75,
       145.  , 145.25, 145.5 , 145.75, 144.25, 144.5 , 144.75, 145.  ,
       145.25, 145.5 , 145.75, 144.25, 144.5 , 144.75, 145.  , 145.25,
       145.5 , 145.75, 144.25, 144.5 , 144.75, 145.  , 145.25, 145.5 ,
       145.75],
	"hourly": "temperature_2m",
	"start_date": "2023-12-23",
	"end_date": "2024-01-02",
}

df = get_om_data(params)

final_filename = f'cruft/om-{param_name}.csv'
print('saving to', final_filename)
df.to_csv(final_filename)
