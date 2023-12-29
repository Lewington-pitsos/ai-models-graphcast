from matplotlib import pyplot as plt
import numpy as np
import climetlab as cml
import xarray
from statelist import load_predictions

def array_stats(arr):
    stats = {
        'Mean': np.mean(arr),
        'Median': np.median(arr),
        'Standard Deviation': np.std(arr),
        'Variance': np.var(arr),
        'Minimum': np.min(arr),
        'Maximum': np.max(arr),
        'Sum': np.sum(arr),
        '25th Percentile': np.percentile(arr, 25),
        '50th Percentile (Median)': np.percentile(arr, 50),
        '75th Percentile': np.percentile(arr, 75)
    }
    return stats


p = load_predictions("cruft/pred/-16-output")
r = xarray.open_dataset('cruft/era5/-16-era5.nc')
rmses = []
times = []
for i, time in enumerate(p.time.values):
    pred = p.sel(time=time, batch=0)

    try:
        re = r.sel(time=time, number=0, surface=0)

        pred_t2 = pred['2m_temperature'].values - 273.15

        re_t2 = re['t2m'].values - 273.15

        rmse = np.mean((pred_t2 - re_t2)**2)
        rmses.append(rmse)
        times.append(time)
    except KeyError:
        print('no reanalysis for time', time)
plt.plot(times, rmses)


rmses = []
times = []
for i, time in enumerate(p.time.values):
    pred = r.sel(time=p.time.values[0], number=0, surface=0)

    try:
        re = r.sel(time=time, number=0, surface=0)

        pred_t2 = pred['t2m'].values - 273.15
        re_t2 = re['t2m'].values - 273.15

        rmse = np.mean((pred_t2 - re_t2)**2)
        rmses.append(rmse)
        times.append(time)
    except KeyError:
        print('no reanalysis for time', time)
plt.plot(times, rmses)



rmses = []
times = []
for i, time in enumerate(p.time.values):

    try:
        pred = r.sel(time=p.time.values[max(i-1, 0)], number=0, surface=0)
        re = r.sel(time=time, number=0, surface=0)

        pred_t2 = pred['t2m'].values - 273.15
        re_t2 = re['t2m'].values - 273.15

        rmse = np.mean((pred_t2 - re_t2)**2)
        rmses.append(rmse)
        times.append(time)
    except KeyError:
        print('no reanalysis for time', time)
plt.plot(times, rmses)
plt.legend(['graphCast', 'step0', 'step@t-1'])

# tilt x axis labels
plt.xticks(rotation=45)
plt.xlabel('Time')
plt.ylabel('Prediction vs Reanalysis RMSE')
plt.title('RMSE of 2m Temperature Predictions vs Reanalysis')
plt.grid()  

# add a legend 
# plt.legend(['RMSE'])


plt.savefig("cruft/compare.png")