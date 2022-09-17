#Veera want to lose 10 pounds in one month. There are multiple conditions to lose 10 pounds in one month:
#Veera needs to walk 10000 steps daily OR needs to run at least 4 miles a day
#and in addition to those,Veera needs to eat less than 1500 calories daily
#We should create a program to calculate if Veera can loose weight or not 

walking_steps = 5000
running_distance = 4
daily_calory = 1500
can_loose_weight = (walking_steps >= 10000 or running_distance >= 4) and daily_calory < 1500

print("Veera can lose weight:", can_loose_weight)
































