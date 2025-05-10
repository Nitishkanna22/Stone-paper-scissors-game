import random
moves = ("stone", "paper", "scissors")

running = True
while running:
    player = None
    computer = random.choice(moves)
    
    while player not in moves:
        player = input("\nEnter your choice (stone, paper, scissors): ").lower()
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == computer:
        print("The match is a draw!")
    elif (player == "paper" and computer == "stone") or \
         (player == "stone" and computer == "scissors") or \
         (player == "scissors" and computer == "paper"):
        print("Congratulations!!!! You have won.")
    else:
        print("Oops, you have lost the game.")
    
    play_again = input("Play again (yes/no): ").lower()
    if play_again != "yes":
        running = False

print("\nThanks for playing!")
