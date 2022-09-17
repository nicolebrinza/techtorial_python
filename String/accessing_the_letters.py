day = "Saturday"
#      01234567
#      12345678 8 will be the  length of the string day. 
letter5th = day[4]
print(day[4])  # r
print(type(letter5th)) #r

print(len(day)) # 8

# What is the last index number of the day? 
last_index = len(day)-1
print("Last index is",last_index)
day2 = 'Monday'
#If the last two or first two charachters of the day and day2 is same print True

# What will be the index numbers for first two charachters in the string? 
# It will always be 0 and 1

# What will be the index numbers for last two charachters in the string ? 
# length of the string -1 and -2

first_two_chs_of_day = day[0] + day[1]
first_two_chs_of_day2 = day2[0] + day2[1]
# condition below will check if the first two charachters of the string is same or not.
is_first2_same = first_two_chs_of_day == first_two_chs_of_day2

last_two_chs_of_day = day[len(day)-2]+day[len(day)-1] 
last_two_chs_of_day2 = day2[len(day2)-2]+day2[len(day2)-1] 
is_last2_same = last_two_chs_of_day==last_two_chs_of_day2

condition = is_last2_same or is_first2_same
print(condition)