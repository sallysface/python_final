#IL GA EG EM HW 7th hangman

import random
#Isaiah - Making Board
def hangman(wrong)
    if wrong< 1:
        return """|--|
                  |
                  |
                  |
                  |____"""
    elif wrong< 2:
        return """|--|
                  |  O
                  |
                  |
                  |_____"""   
    elif wrong == 3:
        return """
                  |---|
                  |   O 
                  |  /|
                  | 
                  |_____"""
    elif wrong == 4:
        return """
                   |---|
                   |   O
                   |  /|\\
                   |
                   |_____"""
        elif wrong == 5:
            return """
                    |---|
                    |   O
                    |  /|\\
                    |  /
                    |_____"""

        elif wrong == 6:
            return """
                    |---|
                    |   O
                    |  /|\\
                    |  / \\
                    |_____"""
                    

#Eva - Guessing letters
def current(guessed, word):
    blanks = ""
    for letter in word:
        if letter in guessed:
            blanks += letter
        else:
            blanks += "_"
    return
    print(f'Word: \n{blanks} Guesses: \n{guessed}')

def guess():
    word = input("Guesse a letter to start\n").strip().lower()
    return word

#Hannah - Wrong guesses

#Gyan - Blanks

#Enzo - Print/play again rand letter

again = input("do you want to play again?(yes/no)?/n").strip().lower()
if again == "yes":
    main()
else:
    print("thanks for playing.")