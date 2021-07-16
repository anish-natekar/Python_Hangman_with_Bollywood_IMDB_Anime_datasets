from Triple_A_func import Triple_A_display_script as ds
from Triple_A_func import Triple_A_hint_script as hs 
from Triple_A_func import Triple_A_file_script as fs
import random

# By: Anish , (July 6th 2021 , 2:00 PM)
def get_word(datalist):
    '''
       (get_word function):
            By: Anish
            This function gets a random name for the game and converts it to upper case
    '''
    data=fs.datafileread(datalist)
    word = random.choice(data)
    word[0] = word[0].upper()
    return word



def play(word, cat, list_of_hints):
    '''
       (Play function):
           By: Aryan
           Play function is a backend function which simulates the game in the code.
       (Hint Part)
           By: Aditya
           Used to get hint while playing.
           when user types 'hint' it shows hint.
    '''

    # By: Aditya , (July 8th 2021 , 7:00 PM )

    hint_ctr = 0
    # Calculating number of hints alphabets
    hints = len(word) // 8 + 1
    letters_guessed = []                                           #stores guessed letters
    # Adding the hint alphabets
    while (hints):
        rnd = random.choice(word)
        letters_guessed.append(rnd)
        hints -= 1
    # Making up the word string to display





    # By: Anish , (July 7th 2021 , 4:00 PM)

    blank_word = ""
    #this loop will form the string which has some blank words and same random alphabets
    for i in word:
        if (i in letters_guessed):
            blank_word += i
        elif (i.isalpha()):
            blank_word += "~"
        elif (i not in letters_guessed):
            blank_word += i
            letters_guessed.append(i)
        else:
            blank_word += i


    # By:Aryan , (July 7th 2021 , 9:30 PM)

    guessed = False
    words_guessed = []                                             # stores guessed words
    chances = 6
    print(ds.display_hangman(chances))
    print(blank_word)
    print("\n")

    while not guessed and chances > 0:
        guess = input("guess a letter or word: ").upper()                                      
        if guess.isalpha() and len(guess) == 1:                #when input is a letter checks whether the input is alphabet or not
            if guess in letters_guessed:                       #checks whether letter is already guessed
                print("you already tried", guess, "!!")
                print(f"{chances} attempts remaining")

                print(blank_word)
                print(ds.display_hangman(chances))

            elif guess not in word:                            #when guessed letter is not present in actual word
                print(f"Oops, {guess} isn't in the word")
                chances -= 1
                print(f"{chances} attempts remaining")
                letters_guessed.append(guess)
                print(blank_word)
                print(ds.display_hangman(chances))

            else:                                              #when guessed letter is present in actual word
                letters_guessed.append(guess)
                print(f"Well done !!, {guess} is in the word")
                print(f"{chances} attempts remaining")

                present_word = ""

                for i in range(len(word)):
                    if guess == str(word[i]):
                        present_word += guess
                    else:
                        present_word += blank_word[i]
                blank_word = present_word
                print(blank_word)
                print(ds.display_hangman(chances))

                if "~" not in blank_word:                       #when the word is completely guessed
                    guessed = True

            # By: Aditya , (July 8th , 7:00 PM)

        elif guess == "HINT":                                   #when user asks for a hint
            print(hs.hint(list_of_hints, hint_ctr, cat))
            print(f"{chances} attempts remaining")
            print(blank_word)
            print(ds.display_hangman(chances))
            hint_ctr += 1


            # By: Aryan ,(July 8th 2021 , 10:30 PM)

        elif len(guess) == len(word):                            #when length of guess is equal to length of actual word
            if guess in words_guessed:                           #checks whether word is already guessed wrongly
                print("You already tried ", guess, "!")

                print(f"{chances} attempts remaining")
                print("blank_word")
                print(ds.display_hangman(chances))
            elif guess == word:                                  #when word is correctly guessed
                blank_word = word
                guessed = True
                print(blank_word)
            else:                                                #incorrect guess
                words_guessed.append(guess)
                chances -= 1
                print("Oops, that isn't the correct word")

                print(f"{chances} attempts remaining")
                print(blank_word)
                print(ds.display_hangman(chances))
        else:
            # when user gives multiple letter input & it is not equal to length of actual word
            print("invalid input")

            print(blank_word)
            print(ds.display_hangman(chances))
            print("\n")



    if guessed:                                                       # when complete word is guessed
        print(f"Yay!, you guessed it correct, the word is {word}")

    else:                                                             # when user run out of chances
        print(f"Sorry, 0 attempts left, the word was {word} , better luck next time!!")
        print("you scored 0")

    return chances
