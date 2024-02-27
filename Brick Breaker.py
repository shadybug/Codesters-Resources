arrow_speed = 5
rows = 4
columns = 19

colors = ["Chartreuse", "MediumOrchid", "Cyan", "HotPink"]

arrow = codesters.Sprite("arrow_outline",0,-200)
arrow.set_size(0.2)
arrow.set_rotation(-90)

def left_key():
    arrow.set_rotation(arrow.get_rotation()+arrow_speed)
stage.event_key("left", left_key)

def right_key():
    arrow.set_rotation(arrow.get_rotation()-arrow_speed)
stage.event_key("right", right_key)

def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    arrow.set_rotation((-x/4) - 90)
stage.event_mouse_move(mouse_move)

for row in range(rows):
    for col in range(columns):
        bubble = codesters.Circle(col*25-230, 205-row*22, 20, random.choice(colors))



