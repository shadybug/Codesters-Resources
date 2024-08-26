stage.set_background_color("green")

player = codesters.Sprite("dragon")
player.set_size(0.4)
enemy = codesters.Sprite("evilwizard", -100, 100)
enemy.set_size(0.25)

for counter in range(5):
    tree_x = random.randint(-250, 250)
    tree_y = random.randint(-250, 250)
    tree = codesters.Sprite("pinetree2", tree_x, tree_y)
    tree.set_size(0.35)
