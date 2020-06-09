import datetime
currentDate = datetime.datetime.now()
 deadline= input ('birth date (mm/dd/yyyy) ')
        deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
        print ( 'u were born ', deadlineDate)