#User wants to deposit his money into his bank account
#he already has $200 in his account
# he has 3 diff paychecks (300, 600, 350)
#He can only deposit one paycheck at a time
#after he deposit all the money in the account, he bought a phone for $599 and headphones for $299
#Create a python program to calculate his final money in the account
#Use input function to get all the values

bank_acc = 200
paycheck1 = 400
paycheck2 = 600
paycheck3 = 350

print("please deposit your first check ")
first_check = int(input())

bank_acc += first_check

print("please deposit your second check ")
second_check = int(input())

bank_acc += second_check

print("please deposit your third check ")
third_check = int(input())

bank_acc += third_check

print("please enter the dollar amount of phone you want to buy")
phone = int(input())

bank_acc -= phone

print("please enter the dollar amount of headphones you want to buy")
headphones = int(input())

bank_acc -= headphones

print("Your final money in your bank account is", bank_acc)



