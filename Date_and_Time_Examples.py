import datetime

print("Current date & time: ", datetime.datetime.now().strftime("%B,%d  %H:%M"))

print("Current date, time & year: ", datetime.datetime.today().ctime())

print("Current year, date & time: ", datetime.datetime.now())

print("Current year, date & time: ", datetime.datetime.now().strftime('%a %b %H:%M:%S %Y'))

print("Current year, date & time: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

print("Current year: ", datetime.date.today().strftime("%Y"))

print("Month of year: ", datetime.date.today().strftime("%B"))

print("Week number of the year: ", datetime.date.today().strftime("%W"))

print("Weekday of the week: ", datetime.date.today().strftime("%w"))

print("Day of year: ", datetime.date.today().strftime("%j"))

print("Day of the month : ", datetime.date.today().strftime("%d"))

print("Day of week: ", datetime.date.today().strftime("%A"))
