# calculate the number of two days between two dates 
from datetime import date
f_date = date(2014,7,2)
l_date = date(2014,7,11)
difference  = l_date - f_date
print(difference.days)


