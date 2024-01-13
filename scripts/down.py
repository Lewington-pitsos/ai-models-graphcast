import os
import climetlab as cml	
import datetime
from statelist import StateList
import xarray

# p = StateList(datetime.datetime(2023, 11, 17, 6), 91, 6)
# predicted_dates = p.dates_mapped_to_hours(
# 	upper_bound=datetime.datetime(2023, 11, 19, 3)
# )

p = StateList(datetime.datetime(2023, 12, 23, 6), 241, 12)
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

print(all_ds)

filename = 'cruft/20231223-era5.nc'
os.makedirs(os.path.dirname(filename), exist_ok=True)

ds = xarray.concat([d.to_xarray() for d in all_ds], dim='time')
ds.to_netcdf(filename)

print(ds)

# ds = ds.to_xarray()
# ds = ds.isel(time=0)

# print(dir(ds))
# print(ds.var)
# plt.imshow(ds.t2m.squeeze())
# plt.savefig('cruft/era5.png')