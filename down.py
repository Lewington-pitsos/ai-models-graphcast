import numpy as np
from matplotlib import pyplot as plt
import climetlab as cml	
import datetime
from prediction import Prediction
import xarray

p = Prediction(datetime.datetime(2023, 11, 17, 6), 91, 6)
predicted_dates = p.dates_mapped_to_hours(
	upper_bound=datetime.datetime(2023, 11, 19, 3)
)

p = Prediction(datetime.datetime(2023, 11, 7, 6), 241, 6)
predicted_dates = p.dates_mapped_to_hours(
	upper_bound=datetime.datetime(2023, 11, 17, 6)
)


print(predicted_dates)

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



ds = xarray.concat([d.to_xarray() for d in all_ds], dim='time')
ds.to_netcdf('cruft/era5/-16-era5.nc')

print(ds)

# ds = ds.to_xarray()
# ds = ds.isel(time=0)

# print(dir(ds))
# print(ds.var)
# plt.imshow(ds.t2m.squeeze())
# plt.savefig('cruft/era5.png')