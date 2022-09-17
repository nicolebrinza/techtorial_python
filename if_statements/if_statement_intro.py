
num1 = 5
num2 = 7
if num1 < num2 :
    print(f"{num1} is lower than {num2}")

if num2 < num1 :
    print(f"{num2} is lower than {num1}") #this line wont get printed

#if statement will execute next line only when the given condition is true

is_num2_bigger = num2 > num1

if is_num2_bigger:
    print("num2 is bigger than num1")

#ask user to enter a string
# if user enters a string with all lower cases print : you entered correct cases

print("Enter a string")
str = input()
is_Lower = str.islower()
if is_Lower:
    print("you entered correct cases")      #line1
    print("because you entered all lower")   #line2
print("you entered a string")                #line3

#Line 1 and 2 are inside the if statement so they depend on condition,
#  but line#3 is outside the if statement so it will be printed anyway
