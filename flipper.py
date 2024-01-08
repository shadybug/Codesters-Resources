# Variables
sea_level = 40

# Rectangles for sky, sea, and sand
sky = codesters.Rectangle(0, 200, 500, 100, "lightblue")
sea = codesters.Rectangle(0, 0, 500, 300, "cadetblue")
sand = codesters.Rectangle(0, -200, 500, 100, "burlywood")

# Set the sea level
sea.set_top(sea_level)

# Shark sprite
shark = codesters.Sprite("shark")
shark.set_size(0.4)

# Key controls
def left_key():
    shark.set_rotation(shark.get_rotation() + 10)
    
stage.event_key("left", left_key)

def right_key():
    shark.set_rotation(shark.get_rotation() - 10)
    
stage.event_key("right", right_key)

def up_key():
    global sea_level
    sea_level += 5
stage.event_key("up", up_key)

def down_key():
    global sea_level
    sea_level -= 5
stage.event_key("down", down_key)

# Main game loop

def game():
    global sea_level
    while True:
        sea.set_top(sea_level)
        stage.wait(0.01)
game()



