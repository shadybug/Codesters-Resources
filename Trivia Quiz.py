# Setting the stage and sprite
stage.set_background("https://images.pexels.com/photos/807598/pexels-photo-807598.jpeg")
sprite = codesters.Sprite("mantis_a07")

# Score variable
score = 0

# Question 1
choice = sprite.ask("Which of these species does not mimic a flower? (a) Orchid Mantis (b) Crab Spider (c) Flower Bee (d) All of these are flower mimics")

# Check if the question was correct, and increase the score
if choice == "c":
    sprite.say("Correct!")
    score = score + 1
# Otherwise, tell the player they got it wrong
else:
    sprite.say("Incorrect! The correct answer was C.")

# Wait a bit, so the player can see the message
stage.wait(2)

# Question 2
choice = sprite.ask("How many true legs does a caterpillar have? (a) 10 (b) 6 (c) 100 (d) 16")

if choice == "b":
    sprite.say("Correct!")
    score = score + 1
else:
    sprite.say("Incorrect! The correct answer was B.")

stage.wait(2)

# Question 3
choice = sprite.ask("Which insect was the first animal to be sent into space? (a) Soldier Ant (b) Cockroach (c) Jumping Spider (d) Fruit Fly")

if choice == "d":
    sprite.say("Correct!")
    score = score + 1
else:
    sprite.say("Incorrect! The correct answer was D.")

stage.wait(2)

# Tell the player their score
sprite.say(score)
