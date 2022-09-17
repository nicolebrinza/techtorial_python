need = ["pencil", "eraser", "notebook"]

need2 = ["computer", "mouse", "keyboards", "camera"]

need.extend(need2)
print(need)


#Extend method takes the copy of need2 list and adds it to need
#Later on changing the value of need2 will not affect the need because
#we are adding with extend method, we did not exactly use need2, we have used the copy of need2
need2.clear()
print("need 2 is", need2)  #[]

#What happens if you extend list with string?
str = "Techtorial"
list = [1,2,3,4,5]
list.extend(str)
print(list)

#Extend method only works only with iterable objects
#[1, 2, 3, 4, 5, 'T', 'e', 'c', 'h', 't', 'o', 'r', 'i', 'a', 'l']

#list.extend(1234) #it will create an error