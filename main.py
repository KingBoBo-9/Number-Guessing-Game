import random

min_value = int(input("Please enter the lowest possible number: "))
max_value = int(input("Please enter the highest possible number: "))
computer_choice = random.randint(min_value, max_value)
number_of_guesses = 0
number_of_guesses_limit = 10
best_score = number_of_guesses_limit
print(f"\nYou have {number_of_guesses_limit} attempts.\n")


while True:
    try:
        user_input = int(
            input(f"Guess the number (between {min_value} and {max_value}): ")
        )
    except ValueError:
        print("Please enter a number.")
        continue

    if user_input < min_value or user_input > max_value:
        print(f"Please enter a number between {min_value} and {max_value}.")
        continue

    number_of_guesses += 1
    if number_of_guesses >= number_of_guesses_limit:
        print(f"You ran out of attempts! The number was {computer_choice}.")
        break

    if user_input == computer_choice:
        print(f"Congratulations! You guessed the number in {number_of_guesses} attempt{'s' if number_of_guesses != 1 else ''}.")
        if number_of_guesses < best_score:
            best_score = number_of_guesses
            print('New best score!')
        print(f"The current best score is {best_score} guess{'es' if best_score != 1 else ''}.")
        break
    elif user_input > computer_choice:
        print("Too high! Try again.")
    elif user_input < computer_choice:
        print("Too low! Try again.")
