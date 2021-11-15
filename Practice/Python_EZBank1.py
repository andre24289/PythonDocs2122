#Andre Tran
#EZBank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

while app.running == True:
    print(app.balance)
    user.choice = input("Would you like to 1. deposit, 2. withdraw, or 3. end?")
    if user.choice == "1":
        user.deposit = input("How much would you like to deposit?")
        user.deposit = int(user.deposit)
        app.balance += user.deposit
    elif user.choice == "2":
        user.withdraw = input("How much would you like to withdraw?")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.balance:
            print("You do not have enough money")
        else:
            app.balance -= user.withdraw
    elif user.choice == "3":
        app.running = False
    else:
        print("Your choice was invalid")
