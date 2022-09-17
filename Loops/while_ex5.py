#Ask user to enter an integer number
#print multiplication table fir given number

print("Enter a number")
num = int(input())

#To use the loop, I need to find the range
#On which number multiplication table starts?   -> 1
#On which number multiplication table ends?     -> 10

table_num = 1

while table_num < 11:
    print(f"{num} * {table_num} = {num*table_num}")
    table_num +=1 
