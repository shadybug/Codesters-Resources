# Stage and variable setup
stage.set_background("matrix")

score = 0
lives = 3

columns = 7
rows = 4

# Ball and paddle setup
ball = codesters.Sprite("slimeball", 0, -100)
ball.set_size(0.5)

paddle = codesters.Rectangle(0, -200, 100, 10, "black")

# Arrow key movement
def left_key():
    paddle.move_left(20)
stage.event_key("left", left_key)

def right_key():
    paddle.move_right(20)
stage.event_key("right", right_key)

# Launch the ball towards wherever the player clicks
def click():
    x = stage.click_x()
    y = stage.click_y()
    ball.set_y_speed((y + 100)/30)
    ball.set_x_speed(x/30)
    
stage.event_click(click)

# Generate bricks
for row in range(rows):
    for column in range(columns):
        brick = codesters.Rectangle(-190 + column * 65, 200 - row * 40, 50, 25, "black")
