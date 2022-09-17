fruits = ("strawberry", "apple", "orange", "banana", "orange")
print(fruits)

print(type(fruits)) #<class 'tuple'>

print(fruits.index("apple"))   # -> 1

print(fruits.count("orange")) # -> 2

#Accessing elements of a tuple
#we can use index numbers as we did with list

#getting the 3rd element from the tupple

print(fruits[2])

#Using FOR loop with tuples

for element in fruits:
    print(element)   

# strawberry
# apple
# orange
# banana
# orange


fruits = ("strawberry", "apple", "orange", "banana", "orange", "cherry")
#From this tupple print out the first fruit name that has odd length
#If there is no fruit with odd length, print: odd length couldnt be found

odd_fruit = ""
for fruit in fruits:
    if len(fruit) % 2 != 0:
            #i have found odd length
        odd_fruit = fruit
        break
if(odd_fruit!=""):
    print("first odd fruit is", odd_fruit)
else:
    print("odd length couldnt be found")

