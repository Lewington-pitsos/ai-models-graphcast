import os
import climetlab as cml	
import datetime
from statelist import StateList
import xarray

p = StateList(datetime.datetime(2023, 12, 22, 12), 241, 6)
predicted_dates = p.dates_mapped_to_hours(
	upper_bound=datetime.datetime(2024, 1, 7, 23)
)

print('dates to download', predicted_dates)

all_ds = []
for date, hours in predicted_dates:
	ds = cml.load_source(
		"cds",
		"reanalysis-era5-single-levels",
		param=["2t"],
		product_type="reanalysis",
		grid='0.25/0.25',
		date=date,
		time=hours,
	)
	all_ds.append(ds)

filename = 'cruft/20231222-era5.nc'
os.makedirs(os.path.dirname(filename), exist_ok=True)

ds = xarray.concat([d.to_xarray() for d in all_ds], dim='time')
ds.to_netcdf(filename)