choices = ["rock", "paper", "scissors"]

stage.set_background("northernlights")
player = codesters.Sprite("astronaut1", 150, 0)
computer = codesters.Sprite("alien1", -150, 0)

choice = player.ask("Rock, paper, or scissors?")

while choice not in choices:
    choice = player.ask("Rock, paper, or scissors?")

player.load_image(choice)

for counter in range(20):
    computer_choice = random.choice(choices)
    computer.load_image(computer_choice)

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
