# Write the code to check if the student passes the class or not. 
# To be able to pass the class student needs to have at least 65 score from 
# the exams and student need to attend at least 80 percent of all the classes. 
# To calculate the average score we need to take take 20 percent of first exam score 
# and 30 percent of second exam score and 50 percent of third exam score. 
# We are given variables for three exam scores and one variable 
# for attendance to classes. If all conditions are met, print true at the end. If not, print false.

first_exam = 70
second_exam = 90
third_exam = 90
average_score = 20*first_exam/100 + 30*second_exam/100 + 50*third_exam/100

attendancy = 70
is_attendancy_enough = attendancy >= 80
is_avg_score_enough = average_score >= 65

pass_the_class = is_attendancy_enough and is_avg_score_enough

print("Average score of the student is ", average_score)
print("Attandancy of student is ", attendancy)
print("Student will pass the class: ", pass_the_class)

