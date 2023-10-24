stage.set_background_color("green")
stage.disable_all_walls()
road = codesters.Rectangle(0,0,400,500,"gray")

player = codesters.Sprite("car1",0,-200)
player.set_size(.5)

score_text = codesters.Text("Score: 0", -200, 220)
speed_text = codesters.Text("Speed: 0", -200, 190)

obstacles = []
trees = []

speed = -5
score = 0
game_over = False

def left_key(player):
    player.move_left(20)
player.event_key("left", left_key)
player.event_key("a", left_key)

def right_key(player):
    player.move_right(20)
player.event_key("right", right_key)
player.event_key("d", right_key)

def create_obstacle():
    obstacle = codesters.Sprite("pollution", random.randint(-180,180), 350)
    obstacle.set_y_speed(speed)

def main():
    while not game_over:
        create_obstacle()
        stage.wait(.3)
main()
