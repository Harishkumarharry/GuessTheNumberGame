#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from replit import clear
from art import logo

def numberCheck(player, number):
    if player < number:
        print("Too low.")
    elif player > number:
        print("Too high.")
    else:
        print(f"You guessed the correct number. The number was {number}!!!")
        return False

    return True

guessNumber = randint(0,100)
levels = {
    "easy": 10,
    "hard": 5,
}
restartGame = True
print(logo)
print(f"Debug line: {guessNumber}")

while restartGame:
    difficultyLevel = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    numberChance = levels[difficultyLevel]
    statusCheck = True
    
    for chances in range(numberChance):
        if statusCheck:
            print(f"You have {numberChance-chances} attempts to guess the correct number.")
            playerGuess = int(input("Enter your guess: "))
            statusCheck = numberCheck(player= playerGuess, number= guessNumber)

    restartGame = bool(int(input("Want to play again? Type '1' for continue or '0' for exit: ")))
    clear()