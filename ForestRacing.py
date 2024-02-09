stage.disable_all_walls()

grass = codesters.Square(0, 0, 500, "green")
road = codesters.Rectangle(0, 0, 350, 500, "grey")

car = codesters.Sprite("car1", 0, -200)
car.set_size(0.5)

game_over = False

# optional extra code, after you've finished other code:
x_velocity = 0

def left_key(sprite):
    sprite.move_left(20)
    # add other actions...
    
car.event_key("left", left_key)

def right_key(sprite):
    sprite.move_right(20)
    # add other actions...
    
car.event_key("right", right_key)

def create_obstacle():
    asteroid = codesters.Sprite("asteroid",0,300)
    asteroid.set_size(0.5)
    asteroid.set_y_speed(-5)

def main():
    while not game_over:
        create_obstacle()
        stage.wait(1)
main()



