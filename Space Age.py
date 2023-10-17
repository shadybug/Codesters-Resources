#set background
stage.set_background("scrollingspace")

#set up the sprites
p1_sprite = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
p1 = codesters.Sprite(p1_sprite, -220, 0)
p1.set_size(0.1)
p1.lives = 3
p2_sprite = "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"
p2 = codesters.Sprite(p2_sprite, 220, 0)
p2.set_size(0.1)
p2.flip_right_left()
p2.lives = 3


#controls for both ships
def w_key():
    p1.move_up(10)
stage.event_key("w", w_key)
def s_key():
    p1.move_down(10)
stage.event_key("s", s_key)


def up_key():
    p2.move_up(10)
stage.event_key("up", up_key)
def down_key():
    p2.move_down(10)
stage.event_key("down", down_key)

left_firing = False
right_firing = False

#fires a laser for player 1
def left_fire():
    global left_firing
    if left_firing is not True:
        left_firing = True
        laser = codesters.TriangleIso(p1.get_x(), p1.get_y(), 5, 10, "blue")
        laser.turn_right(90)
        laser.set_x_speed(10)
        left_firing = False



