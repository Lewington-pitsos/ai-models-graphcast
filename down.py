from matplotlib import pyplot as plt
import climetlab as cml	

ds = cml.load_source(
	"cds",
	"reanalysis-era5-single-levels",
	param=["2t", "msl"],
	product_type="reanalysis",
	grid='5/5',
	date=["2012-12-12", "2012-12-13"],
	time=["00:00", "12:00"],
)

ds = ds.to_xarray()
ds = ds.isel(time=0)
print(ds.dims)

print(ds.variables)
print(type(ds.msl.values))

plt.imshow(ds.msl.values.squeeze())
plt.savefig('cruft/era5.png')