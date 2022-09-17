#ask user to onter a date in format month/day/year    mm/dd/yyyy
# convert given date like following example:
# 03/06/2017    March 6, 2017
# 07/10/2022    July 10, 2022

print("Enter a date in this format  mm/dd/yyyy")
date = input()

#first 2 characters of the given date will give you the number of month
month = date[0:2]
day = date [3:5]
year = date[-4:]

#In which conditions should I modify the date?
#When the date is tarting with 0, I should remove the 0

day = day.removeprefix("0")

if month == "01":
    print(f"January {day}, {year}")
elif month == "02":
     print(f"February {day}, {year}")
elif month == "03":
     print(f"March {day}, {year}")
elif month == "04":
     print(f"April {day}, {year}")
elif month == "05":
     print(f"May {day}, {year}")
elif month == "06":
     print(f"June {day}, {year}")
elif month == "07":
     print(f"July {day}, {year}")
elif month == "08":
     print(f"August {day}, {year}")
elif month == "09":
     print(f"September {day}, {year}")
elif month == "10":
     print(f"October {day}, {year}")
elif month == "11":
     print(f"November {day}, {year}")
elif month == "12":
     print(f"December {day}, {year}")
