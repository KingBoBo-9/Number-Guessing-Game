# Ask min and max
# start loop

import random

computer_choice = random.randint(1, 100)
number_of_guesses = 0

min_value = int(input("Please enter the lowest possible number: "))
max_value = int(input("Please enter the highest possible number: "))

while True:
    try:
        user_input = int(input('Guess the number (between 1 and 100): '))
    except ValueError:
        print('Please enter a number.')
        continue
    if user_input <= 0 or user_input > 100:
        print('Please enter a number between 1 and 100.')
        continue
    
    number_of_guesses += 1

    if user_input == computer_choice:
        print(f"Congratulations! You guessed the number in {number_of_guesses} attempt{'s' if number_of_guesses != 1 else ''}.")
        break
    elif user_input > computer_choice:
        print('Too high! Try again.')
    elif user_input < computer_choice:
        print('Too low! Try again.')
