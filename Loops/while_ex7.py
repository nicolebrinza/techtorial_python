#ask user to enter 2 numbers, first is greater than the second one.
#Find out sum of all the numbers between given two numbers no inclusive
# first: 7
# second : 3
# 3 4 5 6 7  -> sum of 4  5  6  = 15


print("Enter a number")
num1 = int(input())

print("Enter a number smaller than the previous one")
num2 = int(input())

#Before we get to the sum, lets print all numbers between given 2 numbers
copyOfnum2 = num2
num2 = num2 + 1
sum = 0
while num2 < num1:
    # print("in the loop", num2) 
    sum += num2
    num2 = num2+1
print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}" )
    
    