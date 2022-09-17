#Ask user a given string and duplicate each letter in the given string
# input abc
#output aabbcc


print("Enter a string")
str = input()

duplicated = ""

for l in str:
    duplicated+=l
    duplicated+=l
print(duplicated)

for l in str:
    str+=l
print(str)  #abcabc

#Explained: 

# for l in str:
#     duplicated=duplicated+l
#     print("THis print shows evolution of the duplicated",duplicated)
#     duplicated=duplicated+l
#     print("THis print shows evolution of the duplicated",duplicated)
# print(duplicated)