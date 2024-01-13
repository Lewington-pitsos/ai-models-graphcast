import logging
logging.basicConfig(level=logging.INFO)
from ai_models_graphcast.model import GraphcastModel
from datetime import datetime

date = '20231220' # remove the year
time = 6 # get the time

print(f'casting from {time} on {date}')


model_boi = GraphcastModel(
	input="cds", 
	output="file", 
	download_assets=True, 
	path=f'cruft/ssss-output', 
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
