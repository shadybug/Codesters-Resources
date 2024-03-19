# Stage and variable setup
stage.set_background("matrix")

bricks_broken = 0
lives = 3

columns = 7
rows = 4

# Ball and paddle setup
ball = codesters.Sprite("slimeball", 0, -100)
ball.set_size(0.5)

paddle = codesters.Rectangle(0, -200, 100, 10, "cyan")

# Score display
score_text = codesters.Text("Score = {}".format(bricks_broken), 0, 225, "darkblue")

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
    

# Collision with bricks and paddle
stage.event_click(click)
def collision(sprite, hit_sprite):
    hit_color = hit_sprite.get_color() 
    if hit_color == "black":
        sprite.say("Ouch!")
        
    if hit_color == "cyan":
        ball.set_y_speed(ball.get_y_speed())
ball.event_collision(collision)

# Generate bricks
for row in range(rows):
    for column in range(columns):
        brick = codesters.Rectangle(-190 + column * 65, 200 - row * 40, 50, 25, "black")
