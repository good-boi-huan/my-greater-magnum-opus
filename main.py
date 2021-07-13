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
#   order = input(f"Choose one to buy\nPizza: $10\nCandy: $5\nCar: $500\n")
#   if order.lower() == "pizza":
#     money = money - 10
#   elif order.lower() == "candy":
#     money = money - 5
#   elif order.lower() == "car":
#     money = money - 500
#   print(f"You have bought a {order.lower()} and you have {money} dollars left.")
#   play_again = input("Do you want to buy more? ")
#   if play_again.lower() == "no":
#     break
# if money <= 0:
#   print("You have no more money.")
    

# elif provide an alternate situation
# else is all other situations not 

# Different Seasons
# Winter, spring, summer, fall
# Depending on what the season the user says it is, we want to tend to our garden
# Winter: stay inside
# spring: plant trees
# summer: water trees
# fall: pick apples

# season = input("What season is it now? ")
# if season.lower() == "winter":
#   print("Please stay inside and stay warm.")
# elif season.lower() == "spring":
#   print("Please plant some apple trees.")
# elif season.lower() == "summer":
#   print("Please water your apple trees.")
# elif season.lower() == "fall" or season.lower() == "autumn":
#   print("Please pick your apple trees.")
# else:
#   print("Do you even know your seasons? :|")

# Guess the number project

import random
computer_num = random.randint(0, 10)
tries = 5
attempts = 0
number_off = 0
win = False
play = True

while play == True:
  while tries > 0 and win == False:
    guess = int(input("Enter a number between 0 and 10 "))
    if guess == computer_num:
      attempts = attempts + 1
      print(f"Congratuations! You won! The number is {computer_num}. You guessed the number in {attempts} tries.")
      win = True
    elif guess < computer_num and guess >= 0:
      attempts = attempts + 1
      tries = tries - 1
      far_off = computer_num - guess
      print(f"Unfortunately, the number is too small. You have {tries} tries left. You are {far_off} off of the real number.")
    elif guess > computer_num and guess <= 10:
      attempts = attempts + 1
      tries = tries - 1
      far_off = guess - computer_num
      print(f"Unfortunately, the number is too big. You have {tries} tries left. You are {far_off} off of the real number.")
    else:
      print("Read the freaking instructions again.")
  if tries == 0:
    print("You ran out of tries. You lose. Haha!")
  play_again = input("Do you want to play again (y/n)? ")
  if play_again == "n":
    play = False
  else:
      tries = 5
      attempts = 0
      win = False
      computer_num = random.randint(0, 10)
      play = True
