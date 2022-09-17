list = [11,7,44,6,8]

#Insert a new number 9 on index number 4

list.insert(4,9)
print(list) #[11,7,44,6,9,8]

#insert method has 2 parameteres: the index, and the value of the new element

list.append(33)
print(list) #[11,7,44,6,9,8,33]

list.insert(10, "new element") #If you provide bigger index than you have, it will insert the new element
#at the end of the list

#What do you think its the output?
#This will create an exception
#numbers of arguments for append method is 1
#list.append(4,90)  -> will show ERROR