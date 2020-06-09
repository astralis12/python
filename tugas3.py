#abs bikin integer positif (mutlak)


import datetime
currentDate = datetime.datetime.now()

x = input('do u want to use this age calc ? (y/n)')

while True:
    if x == 'y':
        deadline= input ('birth date (mm/dd/yyyy) ')
        deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
        print ( 'u were born ', deadlineDate)
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

        print(f'u are {x} years, {y}  months, {z}  days old.')

    else:
        break







