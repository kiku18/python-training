import datetime as dt
print (dir(dt))
t=dt.date.today()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(dt.MAXYEAR)
print(dt.MINYEAR)
n=dt.datetime.now()
print(n)
print(n.date())
print(n.year)
print(n.month)
print(n.day)
print(n.time())
print(n.hour)
print(n.minute)
print(n.second)
print(n.microsecond)
print(n.weekday())


# Python code to calculate age in year

bd= int(input("Enter the year of birth:"))
print(t.year-bd)

dt1= dt.date(2021,12,1)
print(dt1)
tt1=dt.time(20,24,47)
print(tt1)
tt2=dt.time(14,23,23)
com=dt.datetime.combine(dt1,tt1)
com1=dt.datetime.combine(dt1,tt2)
print(com)
print(com1)

n1=dt.datetime.now()
print(n1)
print(n1.replace(hour=2))
print(n1.replace(minute=59))
print(n1.replace(second=47))
print(n1.replace(microsecond=480))

import calendar
year=2022
month=7
print(calendar.month(year,month))
print(calendar.calendar(year))
t=dt.date.today()
currentmonth=t.month
print("previous month")
print(calendar.month(t.year,currentmonth-1))
print('current month')
print(calendar.month(t.year,currentmonth))
print('next month')
print(calendar.month(t.year,currentmonth+1))


t4=dt.date.today()
currentmonth=12
if currentmonth==12:
    print("previous month")
    print(calendar.month(t4.year, currentmonth - 1))
    print('current month')
    print(calendar.month(t4.year, currentmonth))
    print('next month is that passing to a new year')
    print(t4.year+1)
    print(calendar.month(t4.year+1, 1))
else:
    print("previous month")
    print(calendar.month(t4.year, currentmonth - 1))
    print('current month')
    print(calendar.month(t4.year, currentmonth))
    print('next month')
    print(calendar.month(t4.year, currentmonth + 1))

























