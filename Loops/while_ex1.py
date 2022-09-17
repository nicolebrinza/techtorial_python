#Ask user to give you a string
#From that string print index numbers of all e's

print("Enter a text")
str = input()

#We can access string elements using their indexes

index = 0

#Index number is always smaller than length of the string
# "Example"
#  0123456
#  1234567

# 7 length of the string

length_of_str = len(str)
while index <length_of_str:
    #I want to access the lement with index number of str[index]
    if str[index] == "e":
        print(f"Index number of e is {index}")
    index +=1