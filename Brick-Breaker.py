# Variables
score = 0
rows = 4
columns = 8
bricks = []

# Sprites
paddle = codesters.Rectangle(0, -220, 80, 15, "blue")
paddle.lives = 3

ball = codesters.Circle(0, 0, 20, "green")

# Reset the ball to its starting position
def ball_reset():
    # Random starting speed (optional)
    xspeed = random.randint(1,5)
    yspeed = 3
    
    ball.set_x_speed(xspeed)
    ball.set_y_speed(yspeed)
ball_reset()

def collision(ball, hit_sprite):
    sprite_color = hit_sprite.get_color()
    
    # Brick collision
    if sprite_color == "red":
        stage.remove_sprite(hit_sprite)
        bricks.remove(hit_sprite)
        ball.set_y_speed(-ball.get_y_speed())
    
    # Paddle collision
    if sprite_color == "blue":
        ball.set_y_speed(-ball.get_y_speed())
ball.event_collision(collision)

# Mouse movement controls
def mouse_move():
    x = stage.mouse_x()
    paddle.set_position(x, -220)
stage.event_mouse_move(mouse_move)

# Create bricks
def create_bricks():
    # 5 columns
    for col in range(7):
        brick = codesters.Rectangle(col * 70 - 210, 220, 60, 25, "red")
        bricks.append(brick)
create_bricks()

# Ending the game
def end_game():
    ball.set_x_speed(0)
    ball.set_y_speed(0)
    stage.remove_all_events()

# Check if we've collided with the floor
def floor_collision():
    if ball.get_y() < -230:
        paddle.lives -= 1
        ball_reset()

# Main game loop
def main():
    while len(bricks) > 0:
        floor_collision()
        stage.wait(0.01)
    gamewon = codesters.Text("You win!")
    end_game()
main()



