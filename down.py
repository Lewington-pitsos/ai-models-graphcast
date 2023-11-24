import numpy as np
from matplotlib import pyplot as plt
import climetlab as cml	

ds = cml.load_source(
	"cds",
	"reanalysis-era5-single-levels",
	param=["2t"],
	product_type="reanalysis",
	grid='5/5',
	date=["2012-12-12", "2012-12-13"],
	time=["00:00", "12:00"],
)

ds = ds.to_xarray()
ds = ds.isel(time=0)

print(dir(ds))
print(ds.var)
plt.imshow(ds.t2m.squeeze())
plt.savefig('cruft/era5.png')