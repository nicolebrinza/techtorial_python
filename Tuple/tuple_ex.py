# You have given a two integer variable change the value of these 2 integers

# first_num = 5
# second_num = 3

#output  first_num = 3
        # second_num = 5


#Solution 1 

# a = 5
# b =3
# temp =a 
# a = b
# b = temp
# print(a)
# print(b)

#Solution 2 - we are unpacking

a = 5
b =3
(b,a) = (a,b)
print(a)
print(b)


