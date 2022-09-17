num1, num2 = 4, 6
print(num1 == num2)  # False

is_numbers_equal = num1 == num2
print(is_numbers_equal)
print(type(is_numbers_equal))

print(is_numbers_equal == (num1 == num2))  # True

print*num1 != 4  # False

comparison = num1 != num2
print(comparison)  # True

b3 = num1 > num2
print(b3)  # False

num1 += 2
# on the line above num1 will take the value 6 since 6 is bigger equals to num2
# the following line output True
print(num1 >= num2)  # True

print(True != True)  # False
print(False == False)  # True

a = "Text1"
b = "Text1"
print(a == b)  # True

b = "text1"
print(a == b)  # False
