############################################
#         Created By - Yitzhakpro          #
############################################


def opening_screen(num_of_tries, max_tries):
    """Prints the Opening Screen, including remaining tries, max tries and starting hangman picture.
    :param num_of_tries: number of tries player did, on start: 0
    :param max_tries: Permanent value of max tries in game, current: 6
    :type num_of_tries: int
    :type max_tries: int
    :return: None
    """
    print("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    """)
    print("Remaining tries: ", num_of_tries)
    print("Max tries: ", max_tries)
    print_hangman(num_of_tries)


def print_hangman(num_of_tries):
    """Prints picture of current hangman depending on number of tries
    :param num_of_tries: number of tries player did
    :type num_of_tries: int
    :return: None
    """
    HANGMAN_PHOTOS = {
        "0": "x-------x",
        "1": """        x-------x
        |
        |
        |
        |
        |""",
        "2": """        x-------x
        |       |
        |       0
        |
        |
        |""",
        "3": """        x-------x
        |       |
        |       0
        |       |
        |
        |""",
        "4": r"""       x-------x
        |       |
        |       0
        |      /|\
        |
        |""",
        "5": r"""       x-------x
        |       |
        |       0
        |      /|\
        |      /
        |""",
        "6": r"""        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |"""
    }
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check if the letter entered is valid
    :param letter_guessed: letter the player guessed
    :param old_letters_guessed: list of all the valid letters the player guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: if the input is valid or not
    :rtype: bool
    """
    if letter_guessed in old_letters_guessed:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif letter_guessed not in "abcdefghijklmnoqrstuvwxyz":
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """trying to update the list of old_letters_guessed, and if not prints the all the letter guessed
    :param letter_guessed: letter the player guessed
    :param old_letters_guessed: list of all the valid letters the player guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: if letter updated in the list(old_letters_guessed)
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(*old_letters_guessed, sep=' -> ')
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """Shows the hidden word with letters and '_'
    :param secret_word: the secret word that was selected at the beginning
    :param old_letters_guessed: list of all the valid letters the player guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: None
    """
    current = ""  # the string that will be printed, secret word in words and '_'
    for letter in secret_word:
        if letter in old_letters_guessed:
            current += letter + " "
        else:
            current += "_ "
    print(current)


def check_win(secret_word, old_letters_guessed):
    """Checks if the player won
    :param secret_word: the secret word that was selected at the beginning
    :param old_letters_guessed: list of all the valid letters the player guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: If the player won or not
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def get_secret_word(location, index):
    """Gets the secret word from a file the user entered his location and gave an index for word in the file
    :param location: the location of the file with the words on the computer
    :param index: the index of the word in the file that the player wants to choose
    :type location: str
    :type index: int
    :return: a word, that will be the secret word for the game
    :rtype: str
    """
    words = open(location, "r")
    words_content = words.read()
    words_splitted = words_content.split("\n")
    words.close()
    return words_splitted[index]


def main():
    FILE_LOCATION = input("Enter a file location: ")
    index_of_word = int(input("Enter the index of the word: "))

    SECRET_WORD = get_secret_word(FILE_LOCATION, index_of_word)
    number_of_tries = 0
    MAX_TRIES = 6
    old_letters_guessed = []
    opening_screen(number_of_tries, MAX_TRIES)
    print()
    show_hidden_word(SECRET_WORD, old_letters_guessed)

    while number_of_tries < MAX_TRIES and not check_win(SECRET_WORD, old_letters_guessed):
        letter_guessed = input("Guess a letter: ").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed in SECRET_WORD:
                show_hidden_word(SECRET_WORD, old_letters_guessed)
            else:
                number_of_tries += 1
                print(":(")
                print_hangman(number_of_tries)
                show_hidden_word(SECRET_WORD, old_letters_guessed)

    if check_win(SECRET_WORD, old_letters_guessed):
        print("You Won!")
    else:
        print("You Lost!")


if __name__ == '__main__':
    main()
