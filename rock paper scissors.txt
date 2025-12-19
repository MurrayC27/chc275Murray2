import random
choices = ('rock', 'paper', 'scissors')

# This tracks the score
player_score = 0
computer_score = 0
tie_score = 0


# This randomly selects the computer's choice
def get_computer_choice():
    return random.choice(choices)


# This displays the choices nicely
def display_choices(player, computer):
    print(f"You threw: {player}")
    print(f"opponent threw: {computer}")


# This determines the winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    if player_choice == 'rock':
        if computer_choice == 'scissors':
            return "player"
        else:
            return "computer"

    if player_choice == 'paper':
        if computer_choice == 'rock':
            return "player"
        else:
            return "computer"

    if player_choice == 'scissors':
        if computer_choice == 'paper':
            return "player"
        else:
            return "computer"
# This updates the score
def update_score(result):
    global player_score, computer_score, ties_core

    if result == "player":
        player_score += 1
        print("You win this round!")

    elif result == "computer":
        computer_score += 1
        print("Computer wins this round!")

    else:
        tie_score += 1
        print("This round is a tie!")
# This shows the current score
def display_score():
    print("Current Score")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {tie_score}")
  # Main game 
def play_rps():
    print("Play Rock Paper Scissors")
   # Player's turn
    while True:
        player_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()

        if player_choice not in choices:
            print("Invalid input. Please enter Rock, Paper, or Scissors.")
        else:
            break

    # Computer's turn
    computer_choice = get_computer_choice()

    # Display choices
    display_choices(player_choice, computer_choice)

    
    result = determine_winner(player_choice, computer_choice)

    # Update score
    update_score(result)

    # Display score
    display_score()


# Runs the game
while True:
    play_rps()

    replay = input("Play again? (Yes/No): ").strip().lower()

    if replay != 'yes':
        print("Final Score")
        display_score()
        print("thank u for playing")