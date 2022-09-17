# create a py program to give most efficient exchange possible using only coins
# quarter 25 cents
# nickel 5cents
# dime is 10 cents
# penny 1 cent

# $1.89
# 7 quarters 1 dime 0 nickels 4 pennies
dollar = 2.96
print(type(dollar))
dollar_amount = dollar * 100

quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1
count_of_q = dollar_amount // quarter_value

print("We need to give back ", count_of_q, "quarters")

remaining_exchange_after_q = dollar_amount % quarter_value
count_of_d = remaining_exchange_after_q // dime_value
print(count_of_d, "dimes")
remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickel = remaining_exchange_after_d // nickel_value
print(count_of_nickel, "nickels")
remaining_after_nickel = remaining_exchange_after_d % nickel_value
count_of_pennies = remaining_after_nickel // penny
print(count_of_pennies, "pennies")
