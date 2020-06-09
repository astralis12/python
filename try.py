
import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
daysLeft = deadlineDate - currentDate


years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

x = abs(yearsInt)
y = abs(monthsInt)
z = abs(daysInt)

print(f'You are  {x} years, {y}  months, {z}  days old.')