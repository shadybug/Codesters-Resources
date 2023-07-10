# Put this code directly after setting the sprite and stage
# Text labels
question = codesters.Text("test question", 0, 180, "white")
a = codesters.Text("A:", -150, 50, "white")
b = codesters.Text("B:", 150, 50, "white")
c = codesters.Text("C:", -150, -50, "white")
d = codesters.Text("D:", 150, -50, "white")

choices = [a,b,c,d]

# choices on the screen
questions = []
answers = []
correct_answers = []

========SEPARATION OF SECTIONS: DO NOT COPY=========

# Replace your for loop, and all other code after it, with this. Don't delete the create_questions() function!
for counter in range (3):
    question.set_text(questions[counter])
    
    a.set_text("A: " + answers[counter][0])
    b.set_text("B: " + answers[counter][1])
    c.set_text("C: " + answers[counter][2])
    d.set_text("D: " + answers[counter][3])
    
    choice = sprite.ask(questions[counter])
    
    # Check if the question was correct, and increase the score
    if choice == correct_answers[counter]:
        sprite.say("Correct!")
        score = score + 1
    # Otherwise, tell the player they got it wrong
    else:
        sprite.say("Incorrect! The correct answer was C.")
    
    # Wait a bit, so the player can see the message
    stage.wait(2)

# Tell the player their score
sprite.say(score)
