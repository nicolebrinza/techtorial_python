#Create a program that will ask user ten full names
#After you get 10 full names, create email version of given 10 names and 
#store it inisde the list and print
# enter fullname
#John Wick
#enter full name
#max white

#["johnwick@gmail.com", "maxwhite@gmail.com",....]

full_names = []
emails = []

for i in range(10):
    print("Enter a fullname")
    f_name = input()
    full_names.append(f_name)
    f_name= f_name.replace(" ","").lower() + "@gmail.com"
    emails.append(f_name)

print(full_names)
print(emails)