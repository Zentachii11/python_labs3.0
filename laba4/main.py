import datetime

tek_data = datetime.datetime.today()
iso_calendar = tek_data.isocalendar()
nedelya = iso_calendar[1]


print(nedelya)