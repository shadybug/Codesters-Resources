p2.flip_right_left()

p1.set_size(0.25)
p2.set_size(0.25)

# stage setup
stage.disable_all_walls()

# player movements
def w_key():
    p1.move_up(20)

def s_key():
    p1.move_down(20)

def up_key():
    p2.move_up(20)

def down_key():
    p2.move_down(20)
    
stage.event_key("w", w_key)
stage.event_key("s", s_key)
stage.event_key("up", up_key)
stage.event_key("down", down_key)

# fire lasers
def d_key():
    fire(p1, 5, "red")

def left_key():
    fire(p2, -5, "orange")
    
stage.event_key("d", d_key)
stage.event_key("left", left_key)

def fire(player, direction, color):
    # Make a laser sprite, start at the player that fired it
    laser = codesters.Rectangle(player.get_x(), player.get_y(), 10, 5, color)
    # Move across the screen
    laser.set_x_speed(direction)
    stage.wait(0.25)
