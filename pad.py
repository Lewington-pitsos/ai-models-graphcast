import logging
logging.basicConfig(level=logging.INFO)
from statelist import StateList
from datetime import datetime

sl = StateList(datetime(2023, 12, 20, 6), 240, step_size=240)

# filename = 'cruft/era5/-16-era5.nc'
# os.makedirs(os.path.dirname(filename), exist_ok=True)

for date in sl.dates_as_strings(upper_bound='now'):
	print(date)
	
	# model_boi = GraphcastModel(
	# 	input="cds", 
	# 	output="file", 
	# 	download_assets=True, 
	# 	path=f'cruft/{date_offset}-output', 
	# 	metadata={}, 
	# 	model_args={}, 
	# 	assets_sub_directory='cruft/',
	# 	assets='cruft/',
	# 	date=date_offset, # tells the model to start at the current time - the offset
	# 	staging_dates = None,
	# 	time=-6,
	# 	debug=True,
	# 	lead_time=48,
	# 	only_gpu=True,
	# 	archive_requests="cruft/archive",
	# 	hindcast_reference_year=None,
	# )

	# model_boi.run()
