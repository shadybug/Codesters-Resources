playing = True

score = 0
my_display = codesters.Display(score, -200, 150)

choices = ["rock", "paper", "scissors", "poop"]

stage.set_background("forest3")
dino = codesters.Sprite("dinosaur")
saur = codesters.Sprite("dinosaur2")
winner = codesters.Text("Rock / Paper / Scissors", 0, 200, "pink")

while playing:
    dino.go_to(-150, 0)
    saur.go_to(150, 0)
    saur.face_backward()
    
    choice = saur.ask("Rock, paper, or scissors?")
    while choice not in choices:
        choice = saur.ask("Rock, paper, or scissors?")
    saur.load_image(choice)
    
    computer_choice = random.choice(choices)
    dino.load_image(computer_choice)
    
    if choice == computer_choice:
        winner.set_text("Tie!")
    elif choice == "rock":
        if computer_choice == "paper":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
            score += 1
    elif choice == "paper":
        if computer_choice == "scissors":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
            score += 1
    else:
        if computer_choice == "rock":
            winner.set_text("Computer wins!")
        else:
            winner.set_text("You win!")
            score += 1
            
    my_display.update(score)

    stage.wait(3)
