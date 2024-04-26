# Stage setup
stage.set_background("castle4")

# Important variables
game_over = False
firing = False

# Player setup
player = codesters.Sprite("dragon", 0, -200)
player.set_size(0.35)
player.lives = 3

# Enemy setup
enemies = []
enemy = codesters.Sprite("evilknight", 0, 0)
enemy.set_size(0.35)

# Player laser
laser = codesters.Sprite("sun", 0, 0)
laser.set_size(0.075)

# Enemy laser
enemy_laser = codesters.Star(0, 0, 5, 10, "blue")

# Key controls
def left_key():
    player.move_left(20)
stage.event_key("left", left_key)

def right_key():
    player.move_right(20)
stage.event_key("right", right_key)



