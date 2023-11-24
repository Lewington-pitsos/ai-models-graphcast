from ecmwf.opendata import Client

client = Client()

for date in [20231120, 20231121, 20231122, 20231123]:
	for time in [0]:
		client.retrieve(
			time=time,
			step=240,
			type="fc",
			param=["2t", "msl"],
			target=f"cruft/odata-{date}-{time}.grib2"
		)