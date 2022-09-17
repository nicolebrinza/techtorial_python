s = set()
print(type(s))

print(s)
s.add("new value")
print(s)

s = {}  # <class 'dict'>

print(type())

#Using set() function, we can convert lists into set
#How can we remove the duplicates from the list below?
list = ["s", "s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print(set1)
#it will remove all duplicates from the given list 
print(type(set1))   # <class 'set'>


# clear()
set1.clear()
print(set1)
print(type(set1))  # <class 'set'>

#copy method

list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print("From line 31",set1)

set2 = set1.copy()
print(set1 == set2)
print("set 2 from line 35",set2)
print(type(set2)) # set





