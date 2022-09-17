nums = [1,2,3,1,2,3,4]

#remove all the the number 2's from the list
#First I can find count of 2's in the list
#I can apply the remove method count times

count = 0

for number in nums:
    if number == 2:
        count+=1
print(count)

#I need to apply the remove method count times
#I need to create the loop that iterates count times

#if the count is 5
#range(count) #0 1 2 3 4

#How many times the loop wil get executed? 
#it will get exwecuted 5 times
for i in range(count):
    nums.remove(2)
print(nums)

#--------------------------------------------------------------------
#solution 2

nums = [1,2,3,1,2,3,4]

#remove all the the number 2's from the list

#I can create a copy of the list
newList = nums.copy()

for number in newList:
    if number == 2:
        nums.remove(2)
print(nums)

