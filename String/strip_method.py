# Let's ask user a one string and remove the spaces in the beginning 
# and end of the string
print("Enter a text")
s = "     "

s = s.strip()

print(s)

s = "     Python is a programming language"
print(s)
print(s.strip())

# In strip method we can provide a charachter and it will 
# remove the  certain charachter if that charachter is in the 
# beginning or end of the string. 

# Let's write phone number in the middle of the # tags
phone_number = "###7773332222##"
print(phone_number.strip("#"))

# Strip method can also work with multiple charachters
# we can specify charachters instead of removing the default space

web_site = "www.techtorial.com"
# get the domain name from this website
# .wcmo
print("Domain name of the website is",web_site.strip(".wcmo"))

# given a gmail address from user, print only the user's 
# mail name 
# For example example@gmail.com -> example 
#             yct@gmail.com -> yct

print("please enter your gmail")
gmail = input()

gmail_name = gmail.strip("@ogaiml.c")
print(gmail_name)

# rstrip method which allows us to just
#  remove trailing part of the string

gmail_name1 = gmail.rstrip("@ogaiml.c")
print(gmail_name1)

# lstrip method which allows us to just
#  remove leading part of the string

# From the given website below, print only domain name and .com
web_site = "www.techtorial.com"

print(web_site.lstrip("www."))

#in the strip method we can easily be mistaken, so we have to make sure
#  and double check which parts it is going to remove