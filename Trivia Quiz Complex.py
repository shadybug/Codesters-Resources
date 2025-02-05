score = 0

questions = ["Which of these is NOT a flower mimic?", "How many true legs does a caterpillar have?"]
print(questions[1])

q1_answers = ["Crab spider", "Orchid mantis", "Flower bee", "All of these are flower mimics"]
q2_answers = ["10", "6", "100", "16"]

# Question 1
question = codesters.Text(questions[0], 0, 150, "black")

a = codesters.Text(q1_answers[0], 0, 100, "black")
b = codesters.Text(q1_answers[1], 0, 50, "black")
c = codesters.Text(q1_answers[2], 0, 0, "black")
d = codesters.Text(q1_answers[3], 0, -50, "black")
