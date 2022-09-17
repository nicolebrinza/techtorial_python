#Create a program to print True if there are enough tickets for the NBA game
#We will have 2 variables: sold tickets and max capacity of the stadium
#If stadium capacity is more than sold tickets we should print True and all the other case we should print False

sold_tickets = 9000
max_capacity = 80000
is_there_space =sold_tickets < max_capacity
print("There are enough tickets:", is_there_space)