a = 234
# find the multiplication of digits of the number a
# 2 * 3 * 4
# number a will always have 3 digits
# when we find remainder with 10, it will give us the last digit of that number
# when I divide the number by 10 it will remove the last digit

last_digit = a % 10
print(last_digit)
# following line will remove the last digit of variable a
a = a // 10
middle_digit = a % 10
a = a // 10
first_digit = a % 10

multiplication = last_digit * middle_digit * first_digit
print("Multiplication result of all digits is ", multiplication)

# integer division will give us only the integer part of the division
# for example 21 / 5 = 4.1 but 21 // 5 = 4
