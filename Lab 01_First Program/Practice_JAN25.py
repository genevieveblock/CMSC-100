import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Size of the rectangle
RECT_WIDTH = 10
RECT_HEIGHT = 10

def draw_whale(position_x,position_y,):
    arcade.draw_circle_filled(position_x - 100, position_y - 195, 80, arcade.color.PALE_AQUA)
    arcade.draw_rectangle_filled(position_x, position_y - 165.5, 230, 100, arcade.color.PALE_AQUA)
    arcade.draw_circle_filled(position_x + 100, position_y - 195, 80, arcade.color.PALE_AQUA)
    arcade.draw_circle_filled(position_x - 300, position_y - 195, 60, arcade.color.PALE_AQUA)
    arcade.draw_circle_filled(position_x - 250, position_y - 195, 60, arcade.color.PALE_AQUA)
    arcade.draw_circle_filled(position_x - 220, position_y - 190, 40, arcade.color.MEDIUM_PERSIAN_BLUE)
    arcade.draw_circle_filled(position_x - 325, position_y - 190, 40, arcade.color.MEDIUM_PERSIAN_BLUE)

def draw_ocean(position_x, position_y,):
    arcade.draw_rectangle_filled(position_x, position_y + 190, 2000, 100, arcade.color.MEDIUM_BLUE)
    arcade.draw_rectangle_filled(position_x, position_y + 90, 2000, 100, arcade.color.MEDIUM_ELECTRIC_BLUE)
    arcade.draw_rectangle_filled(position_x, position_y + 0, 2000, 100, arcade.color.MEDIUM_PERSIAN_BLUE)


def draw_sunset(position_x, position_y):


    arcade.draw_circle_filled(position_x - 400, position_y - 200, 500, arcade.color.AMARANTH_PINK)
    arcade.draw_circle_filled(position_x - 400, position_y - 200, 400, arcade.color.RAJAH)
    arcade.draw_circle_filled(position_x - 400, position_y - 200, 300, arcade.color.SAE)
    arcade.draw_circle_filled(position_x - 400, position_y - 200, 200, arcade.color.PUMPKIN)
    arcade.draw_circle_filled(position_x - 400, position_y - 200, 100, arcade.color.SAFETY_ORANGE)
    arcade.draw_circle_filled(position_x - 400, position_y - 200, 50, arcade.color.YELLOW)

def on_draw(delta_time):


    arcade.start_render()


    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
                                 RECT_WIDTH, RECT_HEIGHT,
                                 arcade.color.MEDIUM_PERSIAN_BLUE)


    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time


    if on_draw.center_x < RECT_WIDTH // 500 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // -500:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 500 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // -500:
        on_draw.delta_y *= -1


on_draw.center_x = 100
on_draw.center_y = 50
on_draw.delta_x = 100
on_draw.delta_y = 50



arcade.set_background_color(arcade.color.PLUM)




def main():

    arcade.open_window("WHALE", 800, 600)

    arcade.set_background_color(arcade.color.PLUM)
    draw_sunset(800, 500)
    draw_ocean(50, 50)
    draw_whale(500, 200)
    arcade.schedule(on_draw, 1 / 80)


    arcade.finish_render()
    arcade.run()
main()
