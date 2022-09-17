#you have 40dollars in your phone account
#After each call you will be charged 5$
#print How much call you can make and print how much money left in the account after each call

amount_of_money = 40
each_call = 5
call_number = 1

while amount_of_money >= each_call:
    print(f"{call_number}th call is made")
    call_number += 1
    amount_of_money = amount_of_money - each_call
    print(f"After the call I have ${amount_of_money} left")