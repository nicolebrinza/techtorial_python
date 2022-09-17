# Ask user to enter an integer number and
#  print out all the divisors of given integer number
# 6 -> divisors of six 1,2,3,6
# 10 -> 1,2,5,10
# 14 -> 1,2,7,14
# 11 -> 1, 11

# Possible dividers of given number.
# starts from 1 -> ends at the given number itself

print("Enter a number")
num = int(input())

possible_divisor = 1
s = ""
while possible_divisor <= num:
    #Since we have the possible divisor, but we are not sure 
    # If we can divide the number or not. 
    #How can I understand if possible_divisor is an actual divisor of the number?
    #if number % possible divisor is 0 it means possible_divisor
    #  is an actual divisor of the number
    if num % possible_divisor==0:
        s+=str(possible_divisor)+", "
    possible_divisor+=1
# Remove suffix only removes if the string is ending with given charachters.
print(s.removesuffix(", "),"are the divisors of the number")
#I want to print all divisors in one line like following example
#"1,2,3,6 are the divisors of the number"