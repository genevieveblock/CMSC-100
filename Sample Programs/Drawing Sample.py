import arcade
def draw_tree(position_x,position_y):

arcade.draw_rectangle_filled(position_x,position_y+30,30,60,arcade.color.BLUE_GRAY)

arcade.open_window("pretty",800,600)
arcade.set_background_color(arcade.color.GREEN)
arcade.start_render()
draw_tree(60,300)
arcade.finish_render()
arcade.run()




