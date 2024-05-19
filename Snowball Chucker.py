# sprite setup
stage.set_background("space5")
stage.disable_all_walls()

player = codesters.Sprite("ufo3", -200, -200)
player.set_size(0.3);

enemy = codesters.Sprite("ufo", 200, 200)
enemy.set_size(0.3);

# variables
game_over = False
player.lives = 5
enemy.lives = 5

firing = False # firing cooldown (optional)
enemy_time = 0 # enemy firing cooldown (optional)

# movement
def right_key():
    player.move_right(20)
stage.event_key("d", right_key)

def left_key():
    player.move_left(20)
stage.event_key("a", left_key)

def up_key():
    player.move_up(20)
stage.event_key("w", up_key)

def down_key():
    player.move_down(20)
stage.event_key("s", down_key)

# firing player stars
def click():
    # get the x and y positions of the mouse
    x = stage.click_x()
    y = stage.click_y()
    
    player_star = codesters.Star(player.get_x(), player.get_y(), 4, 10, "skyblue")
    
    aiming(player_star, player, x, y)
stage.event_click(click)

# aims towards the target (x, y) using the pythagorean theorem
def aiming(projectile, cannon, x, y):
    # get the distance from the firing sprite (cannon)
    # to the destination (x, y) as a vector
    vx = x - cannon.get_x()
    vy = y - cannon.get_y()
    
    # calculate the hypotenuse (the magnitude of the vector)
    hypotenuse = math.sqrt(vx * vx + vy * vy)
    
    # normalize the vector (make it a vector with a magnitude of 1)
    normx = vx / hypotenuse
    normy = vy / hypotenuse
    
    # fire the projectile!
    projectile.set_x_speed(normx * 5)
    projectile.set_y_speed(normy * 5)

# main game loop
def main_game():
    while True:
        # firing stars from the enemy every 1 second
        enemy_star = codesters.Star(enemy.get_x(), enemy.get_y(), 4, 10, "lightcoral")
        aiming(enemy_star, enemy, player.get_x(), player.get_y())
        stage.wait(1)

main_game()



