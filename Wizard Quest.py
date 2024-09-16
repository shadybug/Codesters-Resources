# Stage setup
stage.set_background_color("green")
stage.disable_all_walls()

# Player setup (dragon)
player = codesters.Sprite("dragon")
player.set_size(0.4)

# Enemy setup (wizard)
enemy = codesters.Sprite("evilwizard", -100, 100)
enemy.set_size(0.25)

# List to keep track of all non-player sprites
all_sprites = []

# Create trees at random locations and add them to the list
def create_scenery():
    for counter in range(5):
        tree_x = random.randint(-250, 250)
        tree_y = random.randint(-250, 250)
        tree = codesters.Sprite("pinetree2", tree_x, tree_y)
        tree.set_size(0.35)
        all_sprites.append(tree)
create_scenery()

# Movement - this moves all sprites around the player,
# the player stays in the center of the screen
def up_key():
    enemy.move_down(20)
    for sprite in all_sprites:
        sprite.move_down(20)
stage.event_key("w", up_key)

def down_key():
    enemy.move_up(20)
    for sprite in all_sprites:
        sprite.move_up(20)
stage.event_key("s", down_key)

def left_key():
    enemy.move_right(20)
    for sprite in all_sprites:
        sprite.move_right(20)
stage.event_key("a", left_key)

def right_key():
    enemy.move_left(20)
    for sprite in all_sprites:
        sprite.move_left(20)
stage.event_key("d", right_key)

# Interval event that causes the enemy to rotate every 2 seconds
# (setup for attacking/moving code)
def enemy_fire():
    enemy.turn_left(15)
stage.event_interval(enemy_fire, 2)
