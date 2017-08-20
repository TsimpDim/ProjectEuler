days_in_months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

sundays = 0
day_of_week = 1
year = 1901

while(year < 2000):
    if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) : 
        days_in_months[2] = 29
    else:
        days_in_months[2] = 28
    
    for month in range(1,13):
        for day in range(1,days_in_months[month]+1):
            if(day == 1 and day_of_week == 0):
                sundays += 1
            
            day_of_week = (day_of_week + 1)%7
    year += 1

    
print(sundays)

