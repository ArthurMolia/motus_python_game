# Imports :
# for the Wiktionary scrape
from bs4 import BeautifulSoup
import requests

# argument parser
import argparse

# to clear the terminal
from os import system

# to print with colors
class Colors:
    """
    Class Colors - colors the text to be printed with ANSI
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Misc       : from https://www.geeksforgeeks.org/print-colors-python-terminal/
    ---------------------------------------------------------
    """
    reset='\033[0m'
    
    red='\033[41m\033[37m\033[01m'
    yellow='\033[43m\033[30m\033[01m'
    black='\033[40m\033[37m\033[01m'
            
# Functions :
def get_rid_of_special(word):
    """
    Function get_rid_of_special - gets rid of special characters
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : word : word to process
    Misc       : Not the prettiest function, I must admit
    ---------------------------------------------------------
    """
    # list of special characters
    special_characters = "ÀÂÇÉÈÊËÎÏÔÙÛÜŸÑ"

    # new_word = []
    new_word = ""

    for i in range(len(word)):
        if word[i] in "ÀÂ":
            new_word = new_word + "A"
            # new_word.append("A")
        elif word[i] == "Ç":
            new_word = new_word + "C"
            # new_word.append("C")
        elif word[i] in "ÉÈÊË":
            new_word = new_word + "E"
            # new_word.append("E")
        elif word[i] in "ÎÏ":
            new_word = new_word + "I"
            # new_word.append("I")
        elif word[i] == "Ô":
            new_word = new_word + "O"
            # new_word.append("O")
        elif word[i] in "ÙÛÜ":
            new_word = new_word + "U"
            # new_word.append("U")
        elif word[i] == "Ÿ":
            new_word = new_word + "Y"
            # new_word.append("Y")
        elif word[i] == "Ñ":
            new_word = new_word + "N"
            # new_word.append("N")
        else:
            new_word = new_word + word[i]
            # new_word.append(word[i])

    return str(new_word)

def get_random_word(min, max, language):
    """
    Function get_random_word - gets a random word from Wiktionary
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : min : minimum word length
                 max : maximum word length
                 language : word's language
    Misc       : From Wiktionary's French dictionary
    ---------------------------------------------------------
    """ 

    is_valid = False

    # URL to scrape
    if language == "en":
        url = "https://en.wiktionary.org/wiki/Special:RandomInCategory/English_lemmas#English"
    elif language == "es":
        url = "https://en.wiktionary.org/wiki/Special:RandomInCategory/Spanish_lemmas#Spanish"
    elif language == "it":
        url = "https://en.wiktionary.org/wiki/Special:RandomInCategory/Italian_lemmas#Italian"
    elif language == "eus":
        url = "https://en.wiktionary.org/wiki/Special:RandomInCategory/Basque_lemmas#Basque"
    # default language is French
    else:
        url = "https://en.wiktionary.org/wiki/Special:RandomInCategory/French_lemmas#French"

    print("Choix du mot en cours...")
    print("(ça peut être long...)")

    while not (is_valid):
        # getting the request from url
        r = requests.get(url)
        
        # converting the text
        s = BeautifulSoup(r.text, "html.parser")
        
        # finding meta info for title
        word = s.find("h1", class_="firstHeading").text.replace("\n", "")

        word = str.upper(word)

        is_valid = ((min <= len(word) <= max) and ("Œ" not in word) and ("Æ" not in word) and (" " not in word))
    
        word = get_rid_of_special(word)

    # returning the dictionary
    return word

def print_first_clue(word):
    """
    Function print_first_clue - prints the clue for the 1st turn
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : word : game's solution
    Misc       : Remarks...
    ---------------------------------------------------------
    """
    res = ""
    # print(res, end = '')

    for i in range(len(word)):
        if (word[i] in "-'") or (i == 0):
            res_tmp = Colors.red + " " + word[i] + " " 
            # print(res_tmp , end = '')
        else:
            res_tmp = Colors.black + " _ "  
            # print(res_tmp, end = '')
        res = res + res_tmp
    
    res = res + Colors.reset

    return res 

def validation(users_word, true_word):
    """
    Function validation - validate or not the word
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : users_word : the word the user entered
                 true_word  : the word he is seeking 
    Misc       : Prints the user's answer with the indications
                 if the letters are in the word and if
    ---------------------------------------------------------
    """
    colors = []
    # dictionary counting of all the letters in the alphabet
    letter_count = {'A': 0, 'C': 0, 'B': 0, 'E': 0, 'D': 0,
    'G': 0, 'F': 0, 'I': 0, 'H': 0, 'K': 0, 'J': 0, 'M': 0,
    'L': 0, 'O': 0, 'N': 0, 'Q': 0, 'P': 0, 'S': 0, 'R': 0,
    'U': 0, 'T': 0, 'W': 0, 'V': 0, 'Y': 0, 'X': 0, 'Z': 0}

    # checks the letter that are well placed
    for i in range(len(users_word)):
        colors.append(" ")
        letter_count[true_word[i]] += 1
        # if the letter is well placed, the color is red (so R)
        if users_word[i] == true_word[i]:
            colors[i] = "R"
            letter_count[true_word[i]] -= 1

    # checks import letter that are in the word but missplaced
    for i in range(len(users_word)):
        # if the letter is missplaced, the color is yellow (so Y)
        if ((users_word[i] in true_word) 
           and (colors[i] != "R")
           and (letter_count[users_word[i]] > 0)):
            colors[i] = "Y"
            letter_count[users_word[i]] -= 1
        # else there is no color

    # prints the user's answer with the good colors
    res = ""
    # print(res , end = '')
    for i in range(len(users_word)):
        if colors[i] == "R":
            res_tmp = Colors.red + " " + users_word[i] + " " 
            # print(res_tmp , end = '')
        elif colors[i] == "Y":
            res_tmp = Colors.yellow + " " + users_word[i] + " "
            # print(res_tmp, end = '')
        else:
            res_tmp = Colors.black + " " + users_word[i] + " "  
            # print(res_tmp, end = '')
        res = res + res_tmp
    
    res = res + Colors.reset

    return res

def validate_users_input(users_input, word):
    """
    Function validate_users_input - validate the user's input
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : users_input : user's input
                 word : game's solution
    Misc       : Remarks...
    ---------------------------------------------------------
    """
    autorised_characters = "AZERTYUIOPQSDFGHJKLMWXCVBN" + word

    valid_input = True

    for i in range(len(users_input)):
        valid_input = valid_input and (users_input[i] in autorised_characters)
    
    return valid_input and (len(users_input) == len(word))

def game_turn(word):
    """
    Function game_turn - one turn of the game
    
    ---------------------------------------------------------
    
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Parameters : word : the solution
    Misc       : Remarks...
    ---------------------------------------------------------
    """
    valid_input = False

    while not valid_input:  
        users_input = str.upper(input("Entrez votre mot : "))
        valid_input = validate_users_input(get_rid_of_special(users_input), word)

        if not(valid_input):
            print("Votre mot n'est pas valide !")

    to_print = validation(users_input, word)

    return (users_input, to_print)

# Main
if __name__ == "__main__":
    """
    motus.py - Motus game
        
    ---------------------------------------------------------
        
    Author     : Arthur Molia - <moliaarthu@eisti.eu>
    Arguments  : --min : word's minimum length, default 5
                 --max : word's maximum length, default 10
                 --turns : number of turns to find the word,
                           default 5
                 --language : language the word is from,
                              default fr, available :
                                    en, es, it, eus
    Misc       : Remarks...
    ---------------------------------------------------------
    """
    # game's parameters
    parser = argparse.ArgumentParser(description='Game\'s parameters')
    parser.add_argument('--min', type=int, default=5)
    parser.add_argument('--max', type=int, default=10)
    parser.add_argument('--turns', type=int, default=5)
    parser.add_argument('--language', type=str, default="fr")
    args = parser.parse_args()

    min = args.min
    max = args.max
    nbTurns = args.turns
    language = str.lower(args.language)

    # if the user's nbTurns is negative, uses the default value (ie 5)
    if (nbTurns < 1):
        nbTurns = 5

    # if max is strictly inferior to min, invert them
    if (max < min):
        tmp = min
        min = max
        max = tmp

    # calling the function
    word = get_random_word(min, max, language)

    user_answer_history = print_first_clue(word)

    i = 0
    win = False

    while ((i < nbTurns) and (not win)):
        _ = system('clear')

        print(user_answer_history)

        user_answer, to_print = game_turn(word)

        user_answer_history = user_answer_history + "\n" + to_print

        win = user_answer == word

        i += 1

    _ = system('clear')

    print(user_answer_history)
    
    if win:
        print("Bravo, vous avez gagné !")
    else:
        print("Dommage, vous n'avez pas trouvé le mot en " + str(nbTurns) + " tour(s).")
        print("La solution était : '" + word + "'")