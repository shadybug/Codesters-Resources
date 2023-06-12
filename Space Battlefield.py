# Set stage
stage.set_background("matrix")

# Create sprites
p1 = codesters.Sprite("robot7", -150, 150)
p2 = codesters.Sprite("robot_vacuum", 150, -150)
p1.set_size(0.25)
p2.set_size(0.25)

# Health attributes
p1.health = 3
p2.health = 3

# Are the sprites firing?
p1.firing = False
p2.firing = False

# Player 1 movement (arrow keys)
def up_key():
    p1.move_up(20)
stage.event_key("up", up_key)

def down_key():
    p1.move_down(20)
stage.event_key("down", down_key)

def left_key():
    p1.move_left(20)
stage.event_key("left", left_key)

def right_key():
    p1.move_right(20)
stage.event_key("right", right_key)

# Player 2 movement (WASD)
def w_key():
    p2.move_up(20)
stage.event_key("w", w_key)

def s_key():
    p2.move_down(20)
stage.event_key("s", s_key)

def a_key():
    p2.move_left(20)
stage.event_key("a", a_key)

def d_key():
    p2.move_right(20)
stage.event_key("d", d_key)
