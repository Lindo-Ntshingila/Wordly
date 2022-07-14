def game_instruction():
    print("""Wordly is a single player game
    A player has to guess a five letter hidden word
    You have six attempts
    Your Progress Guide "✔❌❌✔➕"
    "✔" Indicates that the letter at that position was guessed correctly
    "➕" indicates that the letter at that position is in the hidden word, but in a different position
    "❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)
   
game_instruction()

def check_word():
    hidden_word = "earth"
    attempt = 6

    while attempt > 0:
        guess = input("Guess today's word: ")

        if guess == hidden_word:
            print("You guessed the word correctly! Congratulations!")
            break
        else:
            attempt = attempt - 1
            print(f"Oops, that is not the correct word. You have {attempt} attempt(s) remaining")
            for char, word in zip(hidden_word, guess):
                if char!=hidden_word[-1]:
                    print(word, end=" ")
                else:
                    print(word)

            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    if char!=hidden_word[-1]:
                        print("✔", end=" ")
                    else:
                        print("✔")
                elif word in hidden_word:
                    if char!=hidden_word[-1]:
                        print("➕", end="")
                    else:
                        print("➕")
                else:
                    if char!=hidden_word[-1]:
                        print("❌", end="")    
                    else:
                        print("❌")

                if attempt == 0:
                    print("Game Over!!")

check_word()
