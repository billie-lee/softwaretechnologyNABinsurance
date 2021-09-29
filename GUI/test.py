from crash_analysis import *

data = Crash_Analysis()

# -----------test for get_keyword(self, start_date, end_date, keyword)
results = data.get_keyword("2014-07-01", "2014-07-01", "Rear end")
print(len(results))

results = data.get_keyword("2014-07-01", "2014-07-01", "Ped hit")
print(len(results))

results = data.get_keyword("2014-07-01", "2014-07-01", "struck")
print(len(results))