import datetime
import random
from Triple_A_func import Triple_A_file_script as fs
from Triple_A_func import Triple_A_backend_script as bs
#By :Anish (July 8th 2021 , 10:00 PM)
def main():
    '''
        (main function)
           By: Anish
              This function integrates all other scripts of game.
              It runs the game.
    '''
    
    # Dictionary to store scoreboard
    score=0
    ScoreBoard={}
    ScoreBoard=fs.readlog()
    # Game Start screen
    while(True):
        print('''
        *****************
        Lets play Hangman
        *****************

        Please select an option:
        1 - Play Hangman
        2 - Score History
        3 - Exit
        ''')
        user=input()
        if(user=="3"):
            exit()
        elif(user=="2"):
            print(ScoreBoard,"\n")
        elif(user=="1"):
            break
        else:
            Print("Invalid input :(")
    # User name entry
    name = input("Please enter your name:")
    print("Hey!,", name, ", Please choose your preferred subject")
    # Intial score of user

    # Game Category selection
    while(True):
        print("Select one of the below given categories\n1) Bollwood (Hinglish)\n2) IMDB >7.4 (English)\n3) MyAnimeList (JapaneseTitlesInEnglish)") 
        try:
            category=int(input())
            if(1<=category<=3):
                break
            else:
                print("Invalid input")
        except(e):
            print("Please Enter Int from 1 to 3\n",e)
    # Category allocated
    datafiles=["Triple_A_bollywoodtext.txt","Triple_A_IMDBtext.txt","Triple_A_MALtext.txt"]
    # Getting random movie title from function
    word = bs.get_word(datafiles[category-1])
    # Game starts here
    score+=bs.play(word[0],category,word[1:])
    # Play again part
    while input("Again? (Y/N) ").upper() == "Y":
        word = bs.get_word(datafiles[category-1])
        score+=bs.play(word[0],category,word[1:])
    dt=datetime.datetime.now()
    print(name+",","your score was =",score,dt,":) Bye Bye")
    # When wanting to stop game we update scoreboard dict
    fs.appendlog(score,name,dt)
    # write dictionary to file
    ###do this
if __name__ == "__main__":
    main()