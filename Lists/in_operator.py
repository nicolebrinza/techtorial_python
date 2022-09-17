#Using IN operator we can check if specified value is in the list(iterable object) or not
#we can also use IN operator for strings as well

list = [1,2,3,4,5]

if 2 in list:
    print("2 is in the list")

if 11 in list:
    print("11 is in the list") #This line won't work cause 11 is not in the list

#NOT IN operator will check if the specified value is not in the iterable objects

if 6 not in list:
    print(6, "is not in the list")

#Ask user to enter a random digit
#check if the digit is present in our list or not
#if user enters present element , print YOU WON A PRIZE,
#if not, print MAYBE NEXT TIME

print("Enter a random digit")
digit = int(input())

if digit in list:
    print("You won a prize")
elif digit not in list:
    print("Maybe next time")

#IN operator can be used for every iterable object