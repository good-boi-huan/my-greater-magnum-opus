# Warm up
# first = input("What is your first name? ")
# last = input("What is your last name? ")
# print(f"Your name in reverse is {last} {first}")

# Loops

# Boolean operators
# Comparision operators
# < (less than)
# > (greater than)
# <= (less than or equal to)
# >= (greater than or equal to)
# == (equal to)
# != (not equal to)
# Let x = 3
# x < 5 (less than) true
# x > 5 (greater than) false
# Let x = 5
# x <= 5 (less than or equal to) true
# x >= 5 (greater than or equal to) true
# x == 5 (equal to) true
# x != 5 (not equal to) false

# Logical operators
# let x = 5 and y = 6
# and if x = 5 and if y = 5 false
# or if x = 5 or if y = 5 true, if x = 6 or if y = 5 false
# not if x is not 5 false, if x is not 4 true

# While loop
# initializing
# counter = 0
# # While loop takes in a boolean expression (T/F)\
# # A while loop will only run if the boolean expression is true

# while(counter < 5):
#   print(counter + 1)
#   counter = counter + 1

# for loop
# counter = 0
# for counter in range(5):
#   print(counter + 1)

# range(5) -> 0, 1, 2, 3, 4
# range(0, 5) -> 0, 1, 2, 3, 4
# range function is inclusive for the left parameter and exclusive for the right parameter

# counter = 5
# for counter in range(0, 5):
#   print(counter + 1)

# List of numbers
# numbers = [1, 2, 3, 4, 5]
# sums = 0
# for numbers in range(1, 6):
#   sums = sums + numbers
# print(sums)

# numbers = [3212983, 32434, 5693, 4, 2323]
# sums = 0
# for value in numbers:
#   sums = sums + value
# print(sums)

# Conditionals
# Definition: if x then y
# Ex: If I go to school, then I learn.
# Ex: If I drink and drive, then I will get into an accident.

# If statements are used for decision making. If statements only run if the boolean expression is true.

# Template
# money = 1000
# while money >= 0:
#   print(f"You have {money} dollars")
#   order = input(f"Choose one to buy\nPizza: $10\nCandy: $5\nCar: $500")
#   if order.lower == "pizza":
#     money = money - 10
#   elif order.lower == "candy":
#     money = money - 5
#   elif order.lower == "car":
#     money = money - 500
#   print(f"You have bought a {order.lower} and you have {money} dollars left.")
#   play_again = input("Do you want to buy more? ")
#   if play_again.lower != "yes":
    

# elif provide an alternate situation
# else is all other situations not 

# Different Seasons
# Winter, spring, summer, fall
# Depending on what the season the user says it is, we want to tend to our garden
# Winter: stay inside
# spring: plant trees
# summer: water trees
# fall: pick apples

season = input("What season is it now? ")
if season.lower() == "winter":
  print("Please stay inside and stay warm.")
elif season.lower() == "spring":
  print("Please plant some apple trees.")
elif season.lower() == "summer":
  print("Please water your apple trees.")
elif season.lower() == "fall" or season.lower() == "autumn":
  print("Please pick your apple trees.")
else:
  print("Do you even know your seasons? :|")