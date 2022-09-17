def sum(*nums):
    sum = 0
    for element in nums:
        sum += element

    return sum

print(sum(1,5,6,8,9))