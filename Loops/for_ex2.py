



print("ENter a number")
num1 = int(input())

print("ENter a number bigger than the first one")
num2 = int(input())
sum = 0
text =""

for n in range(num1, num2):
    if n % 7 == 0 and n % 2 == 0:
        text = text + str(n) + " + "
        sum+=n

print(text.removesuffix(" + "), "=", sum)

