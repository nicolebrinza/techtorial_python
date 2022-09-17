# When we want to reuse the piece of code or algorithm, 
# We create functions and reuse them

#syntax of creating a function is  -> def function_name

def print_name():
    print("Techtorial.")

#Methods only work when they get called

print_name()

#Let's create a method for greeting
#It will take user's name as argument and will print
#"hello user's name"

def print_greeting(name):
    print(f"Hello {name}")

# print("Enter your name")     not a good practice to use input
# user_name = input()
print_greeting("John")

def get_greeting(name):
    return f"Hello {name}"

    #Methods include what is indented but it is recomended to leave 2 lines of space after the last line of method
print(type(get_greeting("Mary")))  #<class 'str'>
greeting = get_greeting("Mary")
print(greeting)

#create a method tp find sum of given two integer
#Add an IF statement in this method so it will error occured
#if type of a or type of b is not float or integer

def sum(a,b):
    addition = a + b
    s = str(type(addition))
    if "int" in s or "float" in s:
        return addition
    else:
        return("Error occured")

    # if type(num1 + num2)
    # return 
# Methods will always stop when the code reaches the return statement. 

print(sum("A", "B"))
print(sum(4,6))

