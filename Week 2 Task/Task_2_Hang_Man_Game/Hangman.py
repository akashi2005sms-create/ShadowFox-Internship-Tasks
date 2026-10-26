import random

hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def play_hangman():
    word_list = ["mango","banana","apple","orange","lychee","plum","dates","guava","cherry","grapes","pear"]
    word_to_play = random.choice(word_list)
    guessed_letters = []
    wrong_guessed_letters = 0
    maximum_attempts = 6  
    print("========================================") 
    print("\n\nHiiiii there, I'm Surya Manikya Sinha :)")   
    print("Welcome to the Hangman Game, where you have to guess a fruit name :)")
    
    while wrong_guessed_letters < maximum_attempts:
        print(hangman_stages[wrong_guessed_letters])
        display_word = ""
        for letter in word_to_play:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"Word: {display_word}")
        
        if "_" not in display_word:
            print(f"\nWINNER! You guessed '{word_to_play}' perfectly!!! Congratulations :)))")
            return
            
        guess = input("\nPlease guess a single letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE VALID LETTER >:(")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter! Try another one.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word_to_play:
            print(f"Yay! '{guess}' is in the word!")
        else:
            print(f"Oh oh! '{guess}' is not in the word!")
            wrong_guessed_letters += 1

    print(hangman_stages[6])
    print(f"Game Over! The secret word was '{word_to_play}'. Better luck next time :-(")


while True:
    play_hangman()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != "yes" and replay != "y":
        print("Thanks for playing. Byeeeeeeeeee :3 ")
        print("========================================")
        break