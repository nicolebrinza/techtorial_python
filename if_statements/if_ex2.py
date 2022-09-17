#ask user to enter a positive integer number
#check if the given number is within 2 of multiple of 10
#If it is within a multiple 10, print Your number is within 2 of a multiple 10
#if not, print your number didnt match the expceted requierement

#10 20 30 40 50
# 21  -> your number is within 2 of a multiple 10
# if the user gives 43 -> your number is within a multiple 10 
# if the user gives 39 -> your number is within 2 of a multiple 10
# We need to use remainder operator.

#If the given number remainder with 10 is less or equals to 2, it means it is within 2 of a multiple 10
# 11 % 10 -> 1
# 22 % 10 -> 2
# 30 % 10 -> 0

print("Enter a number")
number = int(input())
remainder = number%10

if remainder >= 8 or remainder <=2:
    print(number, "is within 2 of a multiple 10")
else:
    print(number, "didnt match the expected requirement")
