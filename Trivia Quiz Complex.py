# Click event
def answer_click(sprite):
    if sprite is correct_answers[0]:
        question.set_text("Correct!")
        score = score + 1

# Register the click event to all text
a.event_click(answer_click)
b.event_click(answer_click)
c.event_click(answer_click)
d.event_click(answer_click)
