#IL GA EG EM HW 7th hangman

import random
#Isaiah - Making Board
def hangman(wrong)
    if wrong< 1:
        return """|--|
                  |
                  |_
                  |__"""
    elif wrong< 2:
        return """|--|
                  |  O
                  |
                  |___"""   
    elif wrong < 3:
        return """|--|
                  |  O
                  |  |
                  |___"""
    
             

#Eva - Guessing letters

#Hannah - Wrong guesses

#Gyan - Blanks

#Enzo - Print/play again rand letter

again = input("do you want to play again?(yes/no)?/n").strip().lower()
if again == "yes":
    main()
else:
    print("thanks for playing.")