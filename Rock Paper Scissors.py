winner = codesters.Text("Hello up here.", 0, 200, "red")

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
