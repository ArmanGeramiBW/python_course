import random

# Get user input for game mode and number of rounds
game = input('Do you want to play with me(computer) or a person?!:(type person or computer)\n')
rounds = int(input("How many Rounds?:\n"))

# Define choices and initialize scores
your_choices = ["p✋","r✊","s✌️"]
player1_points = 0
player2_points = 0

# Define a function to determine the winner of a round
def winner(player1_choice , player2_choice):
    if player1_choice == player2_choice:
        print(f"Both players selected {player1_choice}. It's a tie!")
        #Use or\ in your codes to be easy and beautiful.
    elif (player1_choice == "r" and player2_choice == "s") or \
         (player1_choice == "p" and player2_choice == "r") or \
         (player1_choice == "s" and player2_choice == "p"):
        print(f"{player1_choice} Won from {player2_choice}! Player 1 won!")
        return 1
    else:
        print(f"{player2_choice} won from {player1_choice}! Player 2 won!")
        return 2

# Play against the computer
if game == 'computer':
    for _ in range(rounds):
        computer_choice = random.choice(your_choices)
        player1_choice = input("Rock(r)✊, paper(p)✋, or scissors(s)✌️: Player 1\t") 
        round_winner = winner(player1_choice, computer_choice)
        if round_winner == 1:
            player1_points += 1
        elif round_winner == 2:
            player2_points += 1
    if player2_points > player1_points:
        print("The computer won as always 😈")
    else:
        print("You won but I'll come back 😠")

# Play against a friend
elif game == 'person':
    for j in range(rounds):
        player1_choice = input("Rock(r)✊, paper(p)✋, or scissors(s)✌️: Player 1\t") 
        player2_choice = input("Rock(r)✊, paper(p)✋, or scissors(s)✌️: Player 2\t") 
        round_winner = winner(player1_choice, player2_choice)
        if round_winner == 1:
            player1_points += 1
        elif round_winner == 2:
            player2_points += 1
    if player2_points > player1_points:
        print("Player 2 won the rouds!!!")
    else:
        print("Player 1 won the rouds!!!")
