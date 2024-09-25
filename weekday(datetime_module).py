import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=7, day=18, hour=2)
print(date_of_birth)