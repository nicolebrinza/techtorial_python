s ="Python"
print(s.upper()) # -> PYTHON
print(s) #-> Python

#Since the string is immutable, it will not change its value unless it is reassigned

s = "PYthon"
print(s.lower())

#Method chaining -> as long as the method you use in the string returns another string, you can use other string methods

print(s.lower().upper()) # s will be printed in all upper case since it is the last method

print("Result of swapcase method will be", s.swapcase()) #pyTHON
print("Result of capitalize method will be", s.capitalize()) #Python