#player 1 collision
def collision_left(sprite, hit_sprite):
    laser_color = hit_sprite.get_color() 
    if laser_color == "lime":
        p1.lives -= 1
        sprite.say(p1.lives)
        stage.remove_sprite(hit_sprite)
p1.event_collision(collision_left)

#player 2 collision
def collision_right(sprite, hit_sprite):
    laser_color = hit_sprite.get_color() 
    if laser_color == "mediumpurple":
        p2.lives -= 1
        sprite.say(p2.lives)
        stage.remove_sprite(hit_sprite)
p2.event_collision(collision_right)
