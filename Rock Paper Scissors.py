# Initialization here

while True:
    # Insert code to pick player/computer choices here
    
    winner = codesters.Text("Hello up here.", 0, 200, "white")
    
    if choice == computer_choice:
        winner.set_text("Tie!")
    elif choice == "rock":
        if computer_choice == "paper":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
    elif choice == "paper":
        if computer_choice == "scissors":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
    else:
        if computer_choice == "rock":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
    
    stage.wait(3)
    player.load_image("astronaut1") # Replace with your sprite names
    computer.load_image("alien1") # Replate with your sprite names
    
    stage.remove_sprite(winner)
