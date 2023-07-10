def wall_collision_car(sprite, hit_sprite):
    if hit_sprite.get_color() is "blue":
        if sprite.get_rotation() is 0:
            sprite.move_down(5)
        elif sprite.get_rotation() is 90:
            sprite.move_right(5)
        elif sprite.get_rotation() is 180:
            sprite.move_up(5)
        else:
            sprite.move_left(5)
         
car.event_collision(wall_collision_car)
