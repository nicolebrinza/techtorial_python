#We use 2 methods to remove elements from the set
#discard() method and remove() method

# remove(valueOfTheObject)

set = {3,5,7,9}
# i want to remove number 7 from the set
set.remove(7)
print(set)

#When the element that needs to be remove doesnt exist in the set, it will throw error
#set.remove(7)  #error



# discard(valueOfTheObject) method

set.discard(3)
print(set)
set.discard(3)  #it won't throw error
#When the element that needs to be remove doesnt exist in the set, it will not throw error