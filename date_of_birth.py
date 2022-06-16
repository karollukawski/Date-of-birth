import datetime
import calendar

date_of_birth = input ("Give your date of bith or any date you want (day/month/year): ")

day, month, year = date_of_birth.split("/")

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]
print(day_name)