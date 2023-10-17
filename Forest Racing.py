stage.set_background_color("green")
stage.disable_all_walls()
road = codesters.Rectangle(0,0,400,500,"gray")

player = codesters.Sprite("car1",0,-200)
player.set_size(.5)

sprite = codesters.Text("Score: 0", -200, 220)
sprite = codesters.Text("Speed: 0", -200, 190)

obstacles = []
trees = []

speed = -5
score = 0
game_over = False
