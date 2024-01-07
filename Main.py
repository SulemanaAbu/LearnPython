# Random number
import random
options = ("ROCK", "PAPER", "SCISSORS")
playing = True
while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (Rock, Paper or Scissors): ").upper()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("IT's A TIE")
    elif player == "ROCK" and computer == "SCISSORS":
        print("YOU WIN!")
    elif player == "ROCK" and computer == "PAPER":
        print("YOU LOSE!")
    elif player == "PAPER" and computer == "SCISSORS":
        print("YOU LOSE!")
    elif player == "PAPER" and computer == "ROCK":
        print("YOU WIN!")
    elif player == "SCISSORS" and computer == "ROCK":
        print("YOU LOSE!")
    else:
        print("YOU WIN!")
        break
    if not input("Play again? (Y?N): ").lower() == "y":
        playing = False
    else:
        playing = True

print("Thanks for playing!")

