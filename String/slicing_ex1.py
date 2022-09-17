
#Ask user to enter a string and print a rotated let 2 version
#where the 2 characters moved to the end

#'hello' -> 'lloHe'
#'java' -> 'vaja

from platform import java_ver


print("enter a text")
s = input()
first_two = s[:2]
rest_of_string = s[2:]

s = rest_of_string + first_two
print(s)


