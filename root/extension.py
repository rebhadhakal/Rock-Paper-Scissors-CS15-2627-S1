import random
ties=0
cpu_wins=0
player_wins=0
def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice
def get_player_choice():
    while True:
        player_choice = input("Choose your choice (rock, paper, scissors): ")
        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            return player_choice
def check_winner(cpu_choice, player_choice):
    if cpu_choice == player_choice:
        winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER WON"
        else:
            winner = "CPU WON"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER WON"
        else:
            winner = "CPU WON"
    elif player_choice == "paper":
        winner = "CPU WON"
    else:
        winner = "PLAYER WON"
    return winner
def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)
    return winner
while player_wins <3 and cpu_wins <3:
    while True:
        winner = play_round()
        if winner == "PLAYER WON":
            player_wins = player_wins+ 1
        elif winner == "CPU WON":
            cpu_wins = cpu_wins+ 1
        else:
            ties = ties+ 1
        print(f"Your score:{player_wins}")
        print(f"CPU score: {cpu_wins}")
        if player_wins == 3 or cpu_wins == 3:
            break
if player_wins ==3:
    print("player won the tournament")
if cpu_wins ==3:
    print("cpu won the tournament")