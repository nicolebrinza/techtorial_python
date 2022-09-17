# Every math operation between float and int data type willr esult in flaot data type
floatNum = 3.0
intNum = 5
print("The type of floatNum is", type(floatNum))
print("Type of intNum is", type(intNum))

addition = floatNum + intNum
print("Addition of float and int is", type(addition))

subtraction = intNum - floatNum
print("Subtraction between int and float is", type(subtraction))

multiplication = intNum * floatNum
print("Multiplication between int data type and float is", type(multiplication))

division = intNum / floatNum
print("Division between float and int data type is", type(division))

remainder = floatNum % intNum
print("Remainder between float and int data type is", type(remainder))
remainder2 = intNum % floatNum
print("Remainder between int and float data type is", type(remainder2))

int_division = floatNum // intNum
print("The integer symbol division result between float and integer is ",
      type(int_division))

square_of_float = floatNum * floatNum
print(type(square_of_float))
