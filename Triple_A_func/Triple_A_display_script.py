
# By: Aryan , (July 9th 2021 , 10:00 PM)

def display_hangman(chances):
    '''
       (display_hangman function)
       This function is used to show the stages of hangman getting hanged due to wrong guesses.
       By : Aryan
    '''

    print("    {---------------}" if chances < 6 else "")
    print("    |          ^     " if chances < 6 else "")
    print("    |          " + ("|" if chances < 5 else ""))
    print("    |          " + ("O" if chances < 4 else ""))
    print("    |         " + ("\\|/" if chances < 3 and chances != 0 else "") + ("/|\\" if chances == 0 else ""))
    print("    |          " + ("|" if chances < 2 else ""))
    print("    |         " + ("/ \\" if chances < 1 else ""))
    print("____|____")