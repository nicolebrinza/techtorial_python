t = (1,2,3,4,5,6)
t = list(t)
print(type(t))
print(t)
#from this tuple remove each number if square of the number is smaller than 20

#I can make a copy of t (instead of looping over the t, you loop over the copy of t)
l = t.copy()

for number in l:
    #how can i find the square of he number?
    if number ** 2 < 20:
        t.remove(number)
t = tuple(t)
print(t)
print(type(t))



