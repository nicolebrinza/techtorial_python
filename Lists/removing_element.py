list = ["Python", "C++", "C#", "Java", "Ruby"]

# remove C# from the list

list.remove("C#")
print(list) #["Python", "C++", "Java", "Ruby"]

#I want to remove the second element from this list

list.pop(1)    # pop methos take sonly one parameter
print(list) #["Python", "Java", "Ruby"]

#since -5 is not in the list, it will give index error
# list.pop(-5)
# list.pop(12)  #Index Error: pop index out of range
# print(list)   #Index Error: pop index out of range


#If you use bigger or lower indexes to get elements from iterable objects,
#you will get index out of range error

#print(list[20])

nums = [1,2,3,4,5,6,7]
nums.pop(5)   #will remove the value 6

nums.remove(5) #will remove the value 5

# nums.remove(5) #Error, cause we don't have 5 in the list

nums = [5,1,2,3,5,4,5,6,7]
nums.remove(5) # it will remove only the first 5 

print(list)

