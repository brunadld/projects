import random

def draw_hangman(errors):
    """
    Draws the hangman considering the number of wrong guesses.

    Parameters:
        errors (int): Number of times the user has guessed a letter that isn't included in the final answer.
    """

    for i in range(6):
        for j in range(5):
            match i:
                case 0: print("__", end="")
                case 1:
                    match j:
                        case 0: print("|", end="")
                        case 1: print("\t", end="")
                        case 2: print(" ", end="")
                        case 3: print("|", end="")
                        case 4: print(" ", end="")
                case 2:
                    match j:
                        case 0: print("|", end="")
                        case 1: print("\t", end="")
                        case 2: print(" ", end="")
                        case 3:
                            if errors == 0:
                                print(" ", end="")
                            else:
                                print("O", end="")
                        case 4: print(" ", end="")
                case 3:
                    match j:
                        case 0: print("|", end="")
                        case 1: print("\t", end="")
                        case 2:
                            if errors > 2:
                                print("/", end="")
                            else:
                                print(" ", end="")
                        case 3:
                            if errors > 1:
                                print("|", end="")
                            else:
                                print(" ", end="")
                        case 4:
                            if errors > 3:
                                print("\\", end="")
                            else:
                                print(" ", end="")
                case 4:
                    match j:
                        case 0: print("|", end="")
                        case 1: print("\t", end="")
                        case 2:
                            if errors > 4:
                                print("/", end="")
                            else:
                                print(" ", end="")
                        case 3: print(" ", end="")
                        case 4:
                            if errors > 5:
                                print("\\", end="")
                            else:
                                print(" ", end="")
                case 5:
                    if j == 0:
                        print("|", end="")
                    else:
                        print("___", end="")

        print("\n", end="")

def choose_word():
    """
    Randomly chooses the answer from an existing list of words.

    Returns:
        words[x] (str): The word in the position x of the list of words.
            x (int): Integer chosen randomly between 0 and (n-1).
            n (int): Length of the list.
    """

    # List of possible answers
    words = ["milklove", "junemewnich", "pahnfond", "janjingjing", "namtanfilm", "lingorm"]

    # Picks a random number from 0 to n (length of the list) - 1
    n = words.__len__()
    x = random.randint(0, n-1)

    # Returns the word on the position that was randomly chosen
    return words[x]

def fill_display(answer):
    """
    Fills the display with the number of letters of the answer.

    Parameters:
        answer (str): The final answer of the game.
    
    Returns:
        display (str): Initial display with all spaces empty.
    """

    display = ""

    for i in answer:
        display += "_"

    return display

def print_display(errors, display, letters):
    """
    Prints the number of wrong guesses, the letters already attempted and the updated display.

    Parameters:
        errors (int): Number of times the user has guessed a letter that isn't included in the final answer.
        display (str): The guessed letters and empty spaces.
        letters (str): Wrong guesses from the user.
    """

    print(f"\nERRORS: {errors} \tWRONG GUESSES: {letters}")
    draw_hangman(errors)
    print("\n", end="")

    for i in display:
        print(f"{i} ", end="")

    print("\n")

def update_display(input, answer, display):
    """
    Replaces display with a new string if the input is found in the final answer.
    
    Parameters:
        input (str): Latest letter the user has attempted.
        answer (str): The answer of the game.
        display (str): The guessed letters and empty spaces.
    
    Returns:
        display (str): Updated display if a new letter is added; returns unchanged string otherwise.
    """

    for i in range(answer.__len__()):
        if input == answer[i]:
            display = display[:i] + input + display[i + 1:]

    return display

def check_answer(errors, input, answer):
    """
    Updates the number of mistakes.

    Parameters:
        errors (int): Number of times the user has guessed a letter that isn't included in the final answer.
        input (str): Latest letter the user has attempted.
        answer (str): The answer of the game.
    
    Returns:
        errors (int) unchanged if input is found inside the answer; returns errors + 1 otherwise.
    """

    for i in answer:
        if i == input:
            return errors

    return errors + 1

def update_mistakes(input, letters, answer):
    """
    Updates the wrong guesses if the input isn't in the final answer.

    Parameters:
        input (str): Latest letter the user has attempted.
        letters (str): Wrong guesses from the user.
        answer (str): The answer of the game.
    
    Returns:
        letters (str) unchanged if the final answer contains the input; input is added to letters otherwise.
    """

    for i in answer:
        if i == input:
            return letters

    return letters + " " + input

def game_over(answer, display):
    """
    Checks if the answer was uncovered by comparison between the display and the final answer.

    Parameters:
        answer (str): The answer of the game.
        display (str): The guessed letters and empty spaces.
    
    Returns:
        True if the answer has been uncovered; False otherwise.
    """

    for i in range(answer.__len__()):
        if answer[i] != display[i]:
                return False

    return True

# ----- #

# Randomly chooses a word and fills the display
answer = choose_word()
display = fill_display(answer)

# Prints empty game
print_display(0, display, "")

# Initiates number of errors and the empty string that will contain the wrong guesses
errors = 0
letters = ""

# Loop while the user hasn't reached the maximum number of errors nor guessed the answer
while errors < 6:
    # Prompts the user to pick a letter
    print("Choose a letter:", end=" ")
    user_input = input().lower()[0]

    # Checks if the letter has already been guessed and loops until a new letter is chosen
    while letters.__contains__(user_input) or display.__contains__(user_input):
        print("Letter already attempted, try again! Choose a letter:", end=" ")
        user_input = input().lower()[0]

        # Breaks the loop when a new letter is guessed
        if (letters.__contains__(user_input) or display.__contains__(user_input)) == False:
            break

    # Updates number of errors, wrong guesses and the display
    errors = check_answer(errors, user_input, answer)
    letters = update_mistakes(user_input, letters, answer)
    display = update_display(user_input, answer, display)

    # Prints the game
    print_display(errors, display, letters)

    # Ends the game if the answer is revealed
    if game_over(answer, display) == True:
        break

# Checks if the user won or lost
if game_over(answer, display): print(f"YOU WON! Answer: {answer.upper()}")
else:
    print(f"GAME OVER! Answer: {answer.upper()}")