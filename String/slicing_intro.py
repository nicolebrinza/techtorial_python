
s = "Techtorial"

print(s[4:7])   #tor

print(s[4] + s[7])  

# Ask user to enter a string which length is odd & longer than 3,
#  and print the middle three letters from the string

# "Chicago" -> ica
# "seven" -> eve

print("Enter a string which length is odd & longer than 3")
text = input()

#First I have to find middle index
middle_index = len(text) // 2  #int(len(text)/2)

print(text[middle_index-1:middle_index+1])

#--------------------------------------------

# Ask user to enter a string which length is even & longer than 4,
#  and print the middle 4 letters from the string

# "Techtorial" -> htor
# "keyboard" -> yboa
   

print("Enter a string which length is even & longer than 4")
text2 = input()

middle_index = int(len(text2) /2)
print(text2[middle_index-2:middle_index+2])


