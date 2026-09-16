import random
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
player_wins= 0
cpu_wins= 0
tie= 0
while player_wins <3 and cpu_wins <3:
    winner = play_round()
    if winner == "PLAYER WON":
        player_wins = player_wins +1
        print("You won the round")
    elif winner == "CPU WON":
        cpu_wins = cpu_wins +1
        print("CPU won the round")
    else:
        tie = tie +1
        print("TIE")
    print("Player Wins:", player_wins)
    print("CPU Wins:", cpu_wins)
    print("Ties:", tie)
    print("~~~~~~~~~~~~")
if player_wins == 3:
    print("PLAYER won the game")
else:
    print("CPU won the game")