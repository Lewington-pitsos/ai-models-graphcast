from statelist import StateList
from datetime import datetime

def test_date_strings():
	sl = StateList(datetime(2023, 12, 29, 6), 240, step_size=12)

	dates = sl.dates_as_strings(upper_bound=datetime(2024, 1, 30, 6))

	assert dates[0] == '2023122906'
	assert dates[1] == '2023122918'
	assert dates[2] == '2023123006'

