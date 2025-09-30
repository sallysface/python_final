#IL GA EG EM HW 7th hangman

import random
#Isaiah - Making Board
def hangman(wrong):
    if wrong < 1:
        return """|--|
                  |
                  |
                  |
                  |____"""
    elif wrong == 2:
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
    return f'Word:\n{blanks} Guesses: \n{guessed}'

def guess():
    word = input("Guess a letter\n").strip().lower()
    return word

def main():
     bank = ["poo", "meow", "monkey", "fluroide", 
             "pyonyang","outkast", "isaiah","party","nice", "frog", 
             "princess","sixseven", "femboy", "ducks", "beehive", 
             "ambiguous", "musical", "mango", "mustard" , "fortyone" , 
             "unc", "jba" ,"aot" , "beethoven", "hannah", "abyss", 
             "haiku", "pixel", "pickel", "pajama", "galaxy", "wellspring", 
             "witchcraft", "puppy", "grogginess", "pneumonia", "oxygen", 
             "gossip", "onyx", "calix", "voodoo", "gnarly", "unfixable", 
             "wizard", "microwave", "jaywalk", "rhythem", "iceberg", "titanic", 
             "jazz", "guitar", "buckaroo", "buddy", "embezzeled","fishook", 
             "beekeeper", "ballistic", "maneuver", "resuscitate","judgment", "shorty", "baddie", "doctor"]
#Hannah - Wrong guesses
 
wrong_guesses = 0
guessed_letters = []
current_word = random.choice(bank)
play = "play"
while play == "play":


    print(f"Hangman{wrong_guesses}")


    print(current(guessed_letters, current_word))


    letter = guess()
    guessed_letters.append(letter)


    if letter not in current_word:
      wrong_guesses += 1


#Gyan - Blanks
blanks = ""
for letter in current_word:
    if letter in guessed_letters:
        blanks += letter
else:
    blanks =+"_"
    if blanks == current_word:
        print("You win!")
        play = "win"
        if wrong_guesses >= 6:
            hangman(wrong_guesses)
            print("you lose!")
            play = "lose"
#Enzo - Print/play again rand letter

again = input("do you want to play again?(yes/no)?/n").strip().lower()
if again == "yes":
    main()
else:
    print("thanks for playing.")