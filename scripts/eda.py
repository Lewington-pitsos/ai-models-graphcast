import imageio
import os
import xarray
import climetlab as cml
import matplotlib.pyplot as plt

# ds = cml.load_source("file", "cruft/-6-output")
# for message in ds:
# 	print(message)

# 	print(dir(message))
# 	print(message.datetime())
# 	print(message.offset)
# 	# print all keys of the message
# 	print(message.field_metadata())
# 	print(message.())

# 	break




filename = 'cruft/era5/-16-era5.nc'
ds = xarray.open_dataset(filename)
print(ds)
print(ds.dims)

print('number of timesteps', len(ds.time))
print('start time', ds.time[0])
print('time values', ds.time[0].values)

# slice the xarray so it is just looking at Australia
# australia_only = ds.sel(longitude=slice(110, 160), latitude=slice(-10, -45))
vic = ds.sel(longitude=slice(127, 156), latitude=slice(-26, -44))

img_filenames = []
for idx in range(len(vic.time)):
	timeslice = vic.isel(time=idx)

	plt.imshow(timeslice.t2m.squeeze())
	filename = f'cruft/era5-{idx}.png'
	plt.savefig(filename)
	img_filenames.append(filename)

# save images to gif
images = []
for filename in img_filenames:
	images.append(imageio.imread(filename))
imageio.mimsave('cruft/era5.gif', images, fps=2)