def click():
    player_x = player.get_x()
    player_y = player.get_y()
    player_fire.go_to(player_x, player_y)
    
    x = stage.click_x()
    y = stage.click_y()
    
    x_diff = x - player_x
    y_diff = y - player_y
    
    hypotenuse = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    
    x_norm = x_diff / hypotenuse
    y_norm = y_diff / hypotenuse
    
    player_fire.set_x_speed(x_norm * 5)
    player_fire.set_y_speed(y_norm * 5)
    
stage.event_click(click)
