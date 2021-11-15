# Andre Tran
# Practice using expressions and conditional statements

# An expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

# Functions/methods must be resolved as expressions as well
answer = input("What is your name?")

# Comparison expressions resolve as true or false
print( 7 > 7 )
print ( 7 >= 7 )
print ( x == 10 )

# A conditional statement runs if its condition is True / not False
if answer  == "Andre":
    print("Hello, Andre! Welcome back!")
    print ("This line also prints if your name is Andre")
elif answer == "Vadim":
    print ("Hey! You still owe me money!")
else:
        print("Sorry, I only talk to Andre's")
print ("This line isn't inside of the if statement, and prints regard.")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not true
# ^ You can have as many elif statements as you want
# ^ Else runs if no prior codntions were true

age = input("How old are you?")
age = int(age)
if age >= 10:
    print("Here's your license")

elif age == 9:
    print("You need one more year until you can get your license")

else:
    print ("You are too young")
