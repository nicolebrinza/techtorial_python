number_of_students = 36

str = "Total number of student is {}"  

print(str.format(number_of_students))

number_of_teachers = 12

# create a string that shows number of teachers and 
# number of students

s = "The total number of teacher is {} and the total number of student is {}"
print(s.format(number_of_teachers,number_of_students))

# Using index numbers for formatting the string.
# Index numbers must start from 0
s = "The total number of teacher is {1} and the total number of student is {0}"
print(s.format(number_of_students,number_of_teachers))  # we can give index numbers - that will decide the order


#using f letter
s = f"Total number of teachers is {number_of_teachers}"






























