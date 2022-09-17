#ask user to give you 2 integer numbers
#find the sum of these 2 integer numbers
#if sum of these 2 integer is smaller than 10, print : sum of these two numbers is 10
#if sum of these two number is between 10-19 inclusive, print : sum of these two numbers is 20
#For all the other conditions
#print the actual sum of these two numbers

print("Enter first numer")
num1 = int(input())
print("Enter second numer")
num2 = int(input())
sum = num1 + num2
if sum < 10:
    print("sum of these two numbers is 10")
elif sum >= 10 and sum <= 19:
    print("sum of these two numbers is 20")
else:
    print(sum)

