#set up the sprites
p1_img = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
p2_img = "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"

p1_sprites = ["sharkship_red_bda", "sharkship_yellow_c7e", "sharkship_blue_02d"]
p2_sprites = []

p1_lasers = ["red", "yellow", "blue"]
p2_lasers = ["orange","green","purple"]

p1_color = random.randint(0,2)

p1 = codesters.Sprite(p1_sprites[p1_color], -200, 0)
p2 = codesters.Sprite(p2_img, 200, 0)

########## In the firing code
p1_laser = codesters.Ellipse(p1.get_x(), p1.get_y(), 15, 5, p1_lasers[p1_color])
