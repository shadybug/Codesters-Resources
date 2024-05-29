stage.set_background_color("lightblue")

question_text = codesters.Text(" ", 0, 215)

#create a list to hold all my questions
questions = ["Question 1: Which of these bugs does NOT camouflage among flowers?", "Question 2", "Question 3"]
answers = [["A: Orchid Mantis", "B: Crab Spider", "C: Flower Bee", "D: All of these do"], ["A: "], ["A: "]] #dictionary OR list, key is the index of the question, value are the options for the question
answer_key = ["C", "A", "etc"] #store the correct answers

x = 125
y = 100

option_A = codesters.Text(" ", -x, y)
option_B = codesters.Text(" ", x, y)
option_C = codesters.Text(" ", -x, -y)
option_D = codesters.Text(" ", x, -y)

answers_text = [option_A, option_B, option_C, option_D] 


def ask_questions():
    global question_text, questions
    
    #get a question to ask from the list of questions
    for i in range(len(questions)):
        question = questions[i]
    
        #change the text of the questions-text sprite to update the display
        question_text.set_text(question)
        #then update answers
        update_answers(i)
        debug = input() #to stop after the first question is displayed
    
    
def update_answers(index):
    global answers, answers_text
    #get the answer options from the answers list
    options = answers[index]
    
    for i in range(4):
        answers_text[i].set_text(options[i])
    
#other functions we could use:
def check_answer(choice): #take in the player's choice
    #compare the player's choice to the answer key
    pass
    
    
def main():
    ask_questions()
    
main()
