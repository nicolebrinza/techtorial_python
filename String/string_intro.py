str = "hello"
str1 = "hello"
str2 ="heLlo"
print (str == str1) #True
#equal equal sign is case sensitive, so if cases of two string are different it will return False
print(str == str2) #False

#We can reassign and change the string values as we were able to do with other data types

str2="hello"
print(str2) #hello

#Since we reassign and change the vaue of the str2, equal comparison between str2 and str1 will give the result of True

print(str == str2)  #True

#Concatenating the strings
#Concatenation is adding more string to the existing string value
str2 = str2 + " world"
print(str2) #hello world 

#We can use concatenation even when we are creating the string variable first time

str3 = "hello" + " world"
print(str3) #hello world

str4 = str + str1
print(str4) #hello hello