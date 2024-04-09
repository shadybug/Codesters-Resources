def del_group(bubble, idx):
    # Check right
    if bubble_list[idx + 1].get_color() == bubble.get_color():
        bubble_list[idx + 1].hide()
    # Check left
    if bubble_list[idx - 1].get_color() == bubble.get_color():
        bubble_list[idx - 1].hide()
    # Check up
    if bubble_list[idx - columns].get_color() == bubble.get_color():
        bubble_list[idx - columns].hide()
    # Check down
    if bubble.row < rows and bubble_list[idx + columns].get_color() == bubble.get_color():
        bubble_list[idx + columns].hide()
