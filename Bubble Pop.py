# Setup variables
arrow_speed = 5
rows = 4
columns = 19

# Is the bubble currently firing?
firing = False

# Possible bubble colors
colors = ["Chartreuse", "MediumOrchid", "Cyan", "HotPink"]

# Arrow setup
arrow = codesters.Sprite("arrow_outline",0,-200)
arrow.set_size(0.2)
arrow.set_rotation(-90)

# Firing bubble setup
firing_bubble = codesters.Circle(0, 0, 20, "blue")

# Key controls (left and right arrows)
def left_key():
    arrow.set_rotation(arrow.get_rotation()+arrow_speed)
stage.event_key("left", left_key)

def right_key():
    arrow.set_rotation(arrow.get_rotation()-arrow_speed)
stage.event_key("right", right_key)

# Mouse controls
def mouse_move():
    x = stage.mouse_x()
    arrow.set_rotation((-x/4) - 90)
stage.event_mouse_move(mouse_move)

# Firing controls (up arrow key)
def up_key():
    global firing
    if not firing:
        firing = True
        
        rotation = arrow.get_rotation()
        firing_bubble.set_rotation(rotation + 180)
        
        while firing:
            firing_bubble.move_forward(5)
stage.event_key("up", up_key)

# Collision code
def collision(firing_bubble, hit_sprite):
    global firing
    color = hit_sprite.get_color()
    
    # Check if the bubble hit is the same color as the firing bubble
    if color == firing_bubble.get_color():
        stage.remove_sprite(hit_sprite)
        firing = False
        reset_bubble()
firing_bubble.event_collision(collision)

# Function to send the bubble back to its starting location
def reset_bubble():
    firing_bubble.go_to(0,-200)
    firing_bubble.set_color(random.choice(colors))
reset_bubble()

# Bubble generation loops
for row in range(rows):
    for col in range(columns):
        bubble = codesters.Circle(col*25-230, 205-row*22, 20, random.choice(colors))
