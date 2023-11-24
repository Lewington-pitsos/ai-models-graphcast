import xarray
import climetlab as cml

ds = cml.load_source("file", "cruft/-6-output")
for message in ds:
	print(message)

	print(dir(message))
	print(message.datetime())
	print(message.offset)
	# print all keys of the message
	print(message.field_metadata())
	print(message.())

	break



# ds = xarray.open_dataset('cruft/-6-output-full.nc')

# print(ds)

# print(ds.dims)
# print(ds.batch.values)

# # predictions made starting from 
# print('pred time', len(ds.time))

# # print the start time of this dataset 
# print('start time', ds.time[0])
# # now print the absolute start time of the xarray
# print('abs start time', ds.time[0].values)
