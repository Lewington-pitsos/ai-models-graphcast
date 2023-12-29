import logging
logging.basicConfig(level=logging.INFO)
from ai_models_graphcast.model import GraphcastModel
from statelist import StateList
from datetime import datetime

sl = StateList(datetime(2023, 12, 20, 6), 240, step_size=240)


# filename = 'cruft/era5/-16-era5.nc'
# os.makedirs(os.path.dirname(filename), exist_ok=True)

for dt in sl.dates_as_strings(upper_bound='now'):

	date = dt[:-2] # remove the year
	time = int(dt[-2:]) # get the time

	print(f'casting from {time} on {date}')


	model_boi = GraphcastModel(
		input="cds", 
		output="file", 
		download_assets=True, 
		path=f'cruft/{dt}-output', 
		metadata={}, 
		model_args={}, 
		assets_sub_directory='cruft/',
		assets='cruft/',
		date=date, # just the date part 
		time=time, # just the time part
		staging_dates = None, # alternatively, a list of dates, as opposed to the single date/time
		debug=True,
		lead_time=240, # the number of hours to forcast 
		only_gpu=True,
		archive_requests="cruft/archive",
		hindcast_reference_year=None,
	)

	model_boi.run()
