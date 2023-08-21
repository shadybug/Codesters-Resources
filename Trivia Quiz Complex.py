# INSTRUCTIONS:
# Make another version (copy) of your code
# Title it "Trivia Quiz Final" (or similar)
# Delete everything after the for loop
# Replace it with this code:

def update_text():
    global question_number
    question.set_text(questions[question_number])
        
    a.set_text("A: " + answers[question_number][0])
    b.set_text("B: " + answers[question_number][1])
    c.set_text("C: " + answers[question_number][2])
    d.set_text("D: " + answers[question_number][3])
update_text()

