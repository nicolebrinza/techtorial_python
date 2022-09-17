# In the farm we have 35 cows, 23 chickens, 40 ducks.
# Create a program to calculate total number of legs in the farm
# Requirements: create a variable for cows, chickens, ducks and create variables for theier number of legs
# Print "We have _legs in the farm"
cows = 35
chickens = 23
ducks = 40
legs_of_cow = 4
legs_of_bird = 2

legs = (cows*legs_of_cow + chickens*legs_of_bird + ducks*legs_of_bird)
print("We have ", legs, " legs in the farm")
