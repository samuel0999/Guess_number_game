# Guess random number
import random

# Yes or No
user_input = input("Enter 'yes' to start or 'q' to quit:").lower()

if user_input.lower() != "yes":
    quit()

print("Let's play game :)")

# Attempts
attempts = 0

# Random number generator
rand_num = random.randint(0, 100)

guess_input = int(input("Guess random number between 0-100:"))
attempts += 1

while guess_input != rand_num:
    if guess_input < rand_num:
        print('Too low!')
    else:
        print('Too high!')
    
    guess_input = int(input("Try again:"))
    attempts += 1

print(f"Congratulations! You guessed it! The number was {rand_num}")
print(f"You guessed it in {attempts} attempts.")