import random

computer_choice = random.randint(1, 100)
number_of_guesses = 1 

while True:
    user_input = int(input("Guess the number (between 1 and 100): "))
    if user_input == computer_choice:
        print(f"Congratulations! You guessed the number in {number_of_guesses} attempts.")
        break
    elif user_input > computer_choice:
        print("Too high! Try again.")
        number_of_guesses += 1
    elif user_input < computer_choice:
        print("Too low! Try again.")
        number_of_guesses += 1