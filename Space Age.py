def collision(sprite, hit_sprite):
    my_var = hit_sprite.get_color() 
    if my_var == "lime":
        p1.lives -= 1
        sprite.say(p1.lives)
        stage.remove_sprite(hit_sprite)
p1.event_collision(collision)
