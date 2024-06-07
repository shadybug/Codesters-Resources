MAX_GUESSES = 6 #global var
letters_guessed = []
secret_word = ""
mistakes_made = 0

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_word():
    words = ["cat", "dog", "hamster", "cauldron", "explosion","butterfly", "water", "zebra"]
    
    word = random.choice(words)
    return word
    

def play_hangman():
    global secret_word
    secret_word = get_word()
    #get the users letter guess
    guess = input("Enter a letter: ").lower()
    
    while True: 
        if guess not in alphabet:
            print("That is not a valid letter!")
            guess = input("Please try again: ").lower()
        elif guess in letters_guessed:
            print("You have already guessed that letter.")
            guess = input("Please enter a new letter: ").lower()
        else:
            break
    letters_guessed.append(guess)
    #once we leave the while loop, we have a valid guess
    if check_guess(guess):
        pass
    
def print_guessed():
    #print the users attempted guesses!
    
    pass

def check_guess(guess):
    global secret_word
    if guess in secret_word:
        print("There is a letter {} in the word.")
        return True
    else:
        return False
    
    #check if the letter that the user guessed is in the secret word 
   
def main():
    play_hangman() #start the main game loop!
    
    
main()



