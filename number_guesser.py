import random

def define_answer():
    """Returns a random integer from 1 to 100"""
    return random.randint(1, 100)

def check_answer(n, answer):
    """Prints whether the input is higher or lower than the answer."""
    if n < answer:
        print("Too low! Insert another number [1-100]:", end=" ")
    else:
        print("Too high! Insert another number [1-100]:", end=" ")

def game_over(n, answer):
    """Returns True if the input equals answer; False otherwise."""
    if n == answer: return True
    return False

# ----- MAIN ----- #

# Defines the answer and initializes the number of attempts
answer = define_answer()
attempts = 0

# Asks for the player's initial input
print("Insert an integer from 1 to 100:", end=" ")
user_input = int(input())

# Loops the game until the player guesses the number
while game_over(user_input, answer) == False:
    # Increases the number of attempts
    attempts += 1

    # Checks whether the input is higher or lower than the answer
    check_answer(user_input, answer)
    user_input = int(input())

    # Ends the loop if the answer is guessed
    if game_over(user_input, answer) == True: break

# Prints the number of attempts needed to get to the answer
print(f"\nNumber guessed within {attempts} attempt(s)! Answer: {answer}")