#There are some methods we can compare two sets with each other

s1 = {1,7,9,3}
s2= {2,7,9,5}

#Difference method will get the elements present in set 1 that are not present in set 2

print(s1.difference(s2))  # 1 and 3
print(s2.difference(s1))   # 2 and 5 

#What do you think the return type of difference method?  #set
print(type(s2.difference(s1)))   #    <class 'set'>

#Intersection method will return the common elements in both sets

print(s1.intersection(s2))  # 7 and 9
print(type(s1.intersection(s2)))   #    <class 'set'>

#issubset()
#It checks if given set is present in the other set or not

set = {1,2,3,4,5}
set2 = {2,3,4}
#Since all elements of set2 are in the set, set2 is subset of set

print(set2.issubset(set)) #True
print(set.issubset(set2)) #False

#issuperset()
#it checks if the set is a superset of the given set
#set is a superset of set2
print(set.issuperset(set2)) #True
print(set2.issuperset(set)) #False

#itersection_update
#It will remove all the elements that are not present in the other set
#(removing not common elements)
#intersection_update does not have a return type
s1 = {1,2,3}
s2 = {2, 3}
s1.intersection_update(s2)
print(s1)   # it will print {2,3}

s2.intersection_update(s1)
print(s2) #it won't change the set2

# difference_update
# - it removes the common elements from the set 
# - does not have a return type
s1 = {1,2,3}
s2 = {2, 3}
s1.difference_update(s2)
print(s1)  # it will print {1}  

s3 ={ 1,2,3}
s2.difference_update(s3)
print(s2)  #empty set