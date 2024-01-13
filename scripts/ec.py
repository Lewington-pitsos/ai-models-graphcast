from statelist import load_predictions
import xarray

p = load_predictions("cruft/pred/-6-output")

print(p.time)

# d = xarray.open_dataset('cruft/odata/240-20231117-6.grib2', engine='cfgrib')

# print(d)