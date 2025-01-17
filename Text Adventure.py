options = ["forward", "left", "right", "backward"]

def choices(choice):
    # Handle the player's choice
    # Ask them to re-enter the choice if it's not a word
    # Ask them to re-enter the choice if it's not valid here
    # Give the valid choice back to the function
    if choice in options:
        print("That's a valid choice!")
    else:
        print("That's not valid, try again.")
