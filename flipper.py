# Up key code
def up_key():
    global shark_y_speed
    if sea_level > 0:
        shark_y_speed += math.sin(shark.get_rotation() * math.pi / 180) * shark_swim_power
stage.event_key("up", up_key)

# Main game loop
def game():
    global sea_level, shark_y_speed
    while True:
        sea_level -= shark_y_speed
        sea.set_top(sea_level)
        sand.set_top(sea_level - water_depth)
        
        if sea_level > water_depth:
            shark_y_speed = 5
        elif sea_level > 0:
            shark_y_speed *= 0.95
        else:
            shark_y_speed -= 0.6
        
        
        stage.wait(0.01)
game()
