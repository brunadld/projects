import random

def computer_choice():
    """Returns a random number from 1 to 3."""
    return random.randint(1, 3)

def user_choice():
    """
    Gets the player's choice between rock (1), paper (2) and scissors (3).
    Checks if it's a valid value.

    Returns:
        Integer inserted by the player.
    """
    print("Choose an option:", end="\n\t")
    print("1. Rock", end="\n\t")
    print("2. Paper\n\t3. Scissors")

    # Checks if the value is an integer
    try:
        n = int(input())
    except ValueError:
        print("\nValue entered is not an integer.")
        n = user_choice()

    # Checks if the player picked a valid option
    if n < 1 or n > 3:
        while n < 1 or n > 3:
            print("\nInvalid option!", end=" ")
            n = user_choice()
    
            if n >= 1 and n <= 3:
                break

    return n

def print_choice(x):
    """Converts the player's choice into a string to be printed."""
    match x:
        case 1: return "Rock"
        case 2: return "Paper"
        case 3: return "Scissors"

def tie(comp, user):
    """Returns True if it's a tie; False otherwise"""
    if comp == user: return True
    return False

def winner(comp, user, name):
    """Returns the player's name if they've won the round; "Computer" otherwise."""
    match comp:
        case 1:
            if user == 2: return name
        case 2:
            if user == 3: return name
        case 3:
            if user == 1: return name

    return "Computer"

# ----- MAIN ----- #

# Sets the player's name
print("Player name:", end=" ")
name = input().capitalize()
print("")

# Initializes the number of finished rounds and wins by player
comp_wins = 0
user_wins = 0
rounds = 0

# Loops the game while less than three rounds were concluded
while rounds < 3:
    # Resets the choices for the next round
    user = 0
    comp = 0

    # Loops the round while it's a tie
    while(tie(comp, user) == True):
        user = user_choice()

        # Prints the results
        print(f"\nROUND {rounds + 1}:")
        print(f"{name}: {print_choice(user)}")
        comp = computer_choice()
        print(f"Computer: {print_choice(comp)}")

        # Increases the number of finished rounds and breaks the loop
        if tie(comp, user) == False:
            rounds += 1
            break

        print("It's a tie!\n")

    # Prints the winner of the round
    print(f"{winner(comp, user, name)} wins!\n")

    # Increases the amount of wins of the round's winner
    if winner(comp, user, name) == "Computer": comp_wins += 1
    else: user_wins += 1

    # Breaks the loop if three rounds were concluded
    if rounds == 3:
        break

# Prints the final winner
if user_wins > comp_wins: print(f"{name.upper()} wins!")
else: print("COMPUTER wins!")