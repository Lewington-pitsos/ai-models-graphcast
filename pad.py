import logging
logging.basicConfig(level=logging.INFO)
from ai_models_graphcast.model import GraphcastModel

date_offests = [-6, -16, -26, -36]

for offset in date_offests:
	model_boi = GraphcastModel(
		input="cds", 
		output="file", 
		download_assets=True, 
		path=f'cruft/{offset}-output', 
		metadata={}, 
		model_args={}, 
		assets_sub_directory='cruft/',
		assets='cruft/',
		date=offset,
		staging_dates = None,
		time=12,
		debug=True,
		lead_time=240,
		only_gpu=True,
		archive_requests="cruft/archive",
		hindcast_reference_year=None,
	)

	model_boi.run()
