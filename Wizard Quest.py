# Stage and player setup
stage.set_background_color("black")

player = codesters.Sprite("ufo3")
player.set_size(0.15)

# List of all sprites
all_sprites = []

# Scenery sprite generation
for counter in range(5):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    asteroid = codesters.Sprite("asteroid3", x, y)
    asteroid.set_size(0.25)
    all_sprites.append(asteroid)

# Player movement
def up_key():
    for sprite in all_sprites:
        sprite.move_up(20)
stage.event_key("w", up_key)

def down_key():
    for sprite in all_sprites:
        sprite.move_down(20)
stage.event_key("s", down_key)

def left_key():
    for sprite in all_sprites:
        sprite.move_left(20)
stage.event_key("a", left_key)

def right_key():
    for sprite in all_sprites:
        sprite.move_right(20)
stage.event_key("d", right_key)



