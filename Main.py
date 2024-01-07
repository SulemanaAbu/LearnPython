# Random number
import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
     guess = int(input(f"Enter a number between {low} - {high}: "))
     guesses += 1

     if guess < number:
         print("GUESS IS TOO LOW!")
     elif guess > number:
         print("GUESS IS TOO HIGH!")
     else:
         print("GUESS IS CORRECT!")
         break

print(f"This round took you {guesses} guesses")
