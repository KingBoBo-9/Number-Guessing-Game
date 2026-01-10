import random

computer_choice = random.randint(1, 100)
number_of_guesses = 1 
print(computer_choice)
while True:
    try:
        user_input = int(input('Guess the number (between 1 and 100): '))
    except ValueError:
        print('Please enter a number.')
        continue
    if user_input <= 0:
        print('Please enter a number between 1 and 100.')
    elif user_input == computer_choice:
        print(f'Congratulations! You guessed the number in {number_of_guesses} attempt{'s' if number_of_guesses != 1 else ''}.')
        break
    elif user_input > computer_choice:
        print('Too high! Try again.')
        number_of_guesses += 1
    elif user_input < computer_choice:
        print('Too low! Try again.')
        number_of_guesses += 1