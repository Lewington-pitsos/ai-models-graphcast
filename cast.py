import logging
logging.basicConfig(level=logging.INFO)
from ai_models_graphcast.model import GraphcastModel

date_offests = [-6]

# filename = 'cruft/era5/-16-era5.nc'
# os.makedirs(os.path.dirname(filename), exist_ok=True)

date = 20231229

model_boi = GraphcastModel(
	input="cds", 
	output="file", 
	download_assets=True, 
	path=f'cruft/{date}-output', 
	metadata={}, 
	model_args={}, 
	assets_sub_directory='cruft/',
	assets='cruft/',
	date=date,
	staging_dates = None,
	time=1800,
	debug=True,
	lead_time=48,
	only_gpu=True,
	archive_requests="cruft/archive",
	hindcast_reference_year=None,
)

model_boi.run()
