nums = [1,2,10,11,13,17,21,26]
#from the given list find sum of all the even numbers
#lets find sum of all odds separately
sum = 0
sum_odd = 0
for number in nums:
    if number % 2 == 0:
        sum+= number
    else:
        sum_odd += number

#the variable number will take the last value  #26
print(number)
print("Sum of all even numbers from list is", sum)
print("Sum of all odd numbers from list is", sum_odd)
