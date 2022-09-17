s = {2,2,3,4,5,7}
s2 = {4,10,2,5,44}

#we have function min() and max()
# print(min(s))
# print(max(s2))


#Find out min number of s and multiply with the max number of s2
min = 0     #We assume min =0
max = 0                       
#In the first iteration of the loop I should
#change the value of the min but later on I should only change
#it when the min is bigger than the number

#In the loop below, how can I understand it is te first iteration?

count_of_iteration = 0
for number in s:
    if count_of_iteration == 0:
        min = number
        
    if number < min:
        #If code comes to this line, it means min is bigger than number
        min = number
    count_of_iteration +=1
    

print("Smallest number in set s is",min)


for number in s2:
    if max == 0:
        max =number
    if max < number:
        max=number
print("Biggest number in set s2 is",max)



print("Multiplication is", min * max)

