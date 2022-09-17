#Ask user to enter a password
#If the password doesnt have any uppercase or doesnt have any lower case print False, 
# otherwise print True

print("Type your password")
password = input()

#Password should have upper case and should have lower case
# "password" will be equal to its lower case version

is_there_upper = password != password.lower()

#"PASSWORD" will be equal to its upper case version
#if the password is not equal to its upper case version, it means there is lower case in the string

is_there_lower = password != password.upper()

is_valid_pass = is_there_upper and is_there_lower

print("Your password is valid:", is_valid_pass)
