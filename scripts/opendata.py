from ecmwf.opendata import Client
import datetime
import requests
from statelist import StateList

client = Client()

p = StateList(datetime.datetime(2023, 11, 17, 12), 240, 6)
predicted_dates = p.dates(lower_bound=datetime.datetime(2023, 11, 19, 23, 59, 59))

has_worked_at_least_once = False
worked_count = 0
for (step, d) in predicted_dates:
	day = str(d.year) + str(d.month) + str(d.day)
	try: 
		client.retrieve(
			date=day,
			time=d.hour,
			step=step,
			type="fc",
			param=["2t", "msl"],
			target=f"cruft/odata/{step}-{day}-{d.hour}.grib2"
		)
		print('downloaded', day, d.hour, step)
		has_worked_at_least_once = True
		worked_count += 1
	except requests.exceptions.HTTPError as e:
		print('failed to get', day, d.hour, step, e)
		# if has_worked_at_least_once:
		# 	break

print('downloaded', worked_count, 'files')
