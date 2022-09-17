# ask user to enter a string
#if the given string contains any duplicated letter print: string has duplicated letter
#  otherwise print: string consists of unique letters

print("Enter a string")
str= input()

#we should check for each letterm if there is duplication

is_unique = True
index = 0

while index < len(str):
    if str.count(str[index]) > 1:
        #it means there is duplicated letter
        is_unique = False
        break
    index+=1
    
if is_unique:
    print("String consists of unique letters")
else:
    print("String has duplicated letters")
