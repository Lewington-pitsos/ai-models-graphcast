from ai_models_graphcast.model import GraphcastModel

model_boi = GraphcastModel(
	input="cds", 
	output="file", 
	download_assets=True, 
	path='cruft/', 
	metadata={}, 
	model_args={}, 
	assets_sub_directory='cruft/',
	assets='cruft/',
	date=-5,
	staging_dates = None,
	time=12,
	debug=True,
	lead_time=240,
)

model_boi.run()
