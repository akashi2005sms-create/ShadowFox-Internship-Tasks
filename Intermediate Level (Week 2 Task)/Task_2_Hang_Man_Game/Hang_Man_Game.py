import random

bodystagesofhangman = [
    """
    ----------
    |       |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |       |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |      /|
    |
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |      /|\\
    |
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |      /|\\
    |      /
    |
    |
    ----------
    """,
    """
    ----------
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    |
    ----------
    """
]

def hangmangame():
    word_list = ["mango","banana","apple","orange","lychee","plum","date","guava","cherry","grape","pear","watermelon","lemon","papaya","peach","pineapple","coconut"]
    word_to_play= random.choice(word_list)
    guessed_letters= []
    wrongly_guessed_letters= 0
    maximum_attempts = 6
    print("========================================")
    print("\n\nHiiiiii there, I'm Surya Manikya Sinha :)")
    print("Welcome to the Hangman game where you guess a fruit's name :)")

    while wrongly_guessed_letters < maximum_attempts:
        print(bodystagesofhangman[wrongly_guessed_letters])
        showing_word= ""
        for l in word_to_play:
            if l in guessed_letters:
                showing_word += l + " "
            else:
                showing_word += "_ "

        print(f"The Word: {showing_word}")

        if "_" not in showing_word:
            print(f"\nCongratulations :))) You have guesssed '{word_to_play}' perfectly!!!")
            return

        guess = input("\nPlese guess a letter: ").lower()

        if len(guess) !=1:
            print("Please enter ONLY ONE VALID LETTER  >:(")
            continue

        if guess in guessed_letters:
            print("YOU HAVE ALREADY GUESSED THAT LETTER :| ")
            continue

        guessed_letters.append(guess)

        if guess in word_to_play:
            print(f"Yepiii ! '{guess}' is in the word :)")
        else:
            print(f"Oops ! '{guess}' is not in the word :(")
            wrongly_guessed_letters +=1

    print(bodystagesofhangman[6])
    print(f"Game Over !!! The secret word was '{word_to_play}'.")
    print("Better luck next time :(")

while True:
    hangmangame()
    play_again = input("\nDo you want to play again? Press yes to play or no to quit.").lower()
    if play_again != "yes" and play_again!= "y":
        print("Thanks for playing. Byeeeeeeee :3")
        print("========================================")
        break

      
