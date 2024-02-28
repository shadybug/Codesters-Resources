# Setting up the stage
stage.set_background_color("green")
stage.disable_all_walls()

# Score, speed, and game over variables
score = 0
speed = -5
game_over = False

# Road sprites
road = codesters.Rectangle(0, 0, 400, 500, "grey")
roadline = codesters.Rectangle(0, 0, 10, 500, "yellow")

# Car sprite
car = codesters.Sprite("car1",0,-200)
car.set_size(0.5)

# Left and right movement
def left_key():
    car.move_left(20)
stage.event_key("left", left_key)

def right_key():
    car.move_right(20)
stage.event_key("right", right_key)

# Main game loop (like a "forever" in Scratch)
def main():
    while not game_over:
        oil = codesters.Sprite("pollution", 0, 300)
        oil.set_size(0.5)
        oil.set_y_speed(speed)
        stage.wait(1)
main()
