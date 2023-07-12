# INITIALIZATION HERE

# Main game loop (like a forever loop in Scratch)
while True:
    # INSERT CODE TO PICK PLAYER/COMPUTER CHOICES HERE

    # Make a text label
    winner = codesters.Text("Hello up here.", 0, 200, "white")

    # Check who won with a series of conditionals, and change the text of the label
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

    # Wait a few seconds before resetting
    stage.wait(3)
    player.load_image("astronaut1") # Replace with your sprite names
    computer.load_image("alien1") # Replate with your sprite names

    # Delete the text label so it no longer shows
    stage.remove_sprite(winner)
