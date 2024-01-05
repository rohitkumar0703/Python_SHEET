# Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

'''Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.'''

import datetime 
x = datetime.datetime(2023,5,17)
print(x)

# Diwsplay the name of month
import datetime
x=datetime.datetime(2023,11,15)
print(x.strftime("%B"))