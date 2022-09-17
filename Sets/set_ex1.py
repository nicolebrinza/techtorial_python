# Given two lists a, b. Check if two lists have 
# at least one element common in them.

# Examples:

# Input : a = [1, 2, 3, 4, 5]
#         b = [5, 6, 7, 8, 9]
# Output : True

# Input : a=[1, 2, 3, 4, 5]
#         b=[6, 7, 8, 9]
# Output : False


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

set1 = set(list1)
print(set1)

set2 = set(list2)
print(set2)

#How can I check if ther is common element from these 2 sets?
#In the below I will get common elements from bots sets above
common_elements = set1.intersection(set2) # {5}

#If there is at least one common element what should be the size of common_elements set?
#IT should be at least 1
#len(common_elements) >= 1

# WE can use IF 
# if len(common_elements) >= 1:
#     print("True")
# else:
#     print("False")


# or we can use BOOLEAN
is_there_common = len(common_elements) >= 1
print(is_there_common)