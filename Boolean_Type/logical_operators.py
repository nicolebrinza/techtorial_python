from xmlrpc.client import FastMarshaller


bool1 = True
bool2 = False
bool3 = True
# not operator will make true conditions false, false conditions true

print(not bool3)  # False
print(not bool2)  # True

# False. Since and condition requires both sides to be true for returning true this line will print false
print(bool2 and bool1)

print(bool2 or bool1)  # if one condition is true, or condition will return true

print(bool2 or not bool1)
# it will return false because not operator will make the bool1's value false or False will result in false

print(not bool2 and bool1)
# it will return True because not operator will make the bool2's value true or true will result in true
