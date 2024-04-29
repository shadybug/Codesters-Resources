stage.set_background("cyber_chip_blue")

player_base = codesters.Circle(-200, -200, 250, "lightcoral")
enemy_base = codesters.Circle(200, 200, 250, "skyblue")


enemy = codesters.Sprite("robot7",200,200)
enemy.set_size(0.25)
player = codesters.Sprite("alien1",-200,-200)
player.set_size(0.5)

def right_key():
    if player.get_x() < -100:
        player.move_right(20)
stage.event_key("d", right_key)

def left_key():
    if player.get_x() > -225:
        player.move_left(20)
stage.event_key("a", left_key)

def up_key():
    if player.get_y() < -100:
        player.move_up(20)
stage.event_key("w", up_key)

def down_key():
    if player.get_y() > -225:
        player.move_down(20)
stage.event_key("s", down_key)
