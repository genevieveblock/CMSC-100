import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SQUARE_CENTER = 25
MOVEMENT_SPEED = 3


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

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.sound = arcade.load_sound("laser(1).ogg")

    def draw(self):

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def animate(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x


        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.sound)
class Square:
    def __init__(self, position_x, position_y,change_x, change_y, SQUARE_CENTER, color):


        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.SQUARE_CENTER = SQUARE_CENTER
        self.color = color
        self.sound = arcade.load_sound("laser(1).ogg")

    def draw(self):

        arcade.draw_rectangle_filled(self.position_x, self.position_y, 40, self.SQUARE_CENTER, self.color)
    def animate(self):
        if self.position_x < self.SQUARE_CENTER / 2:
            self.position_x = self.SQUARE_CENTER / 2
            arcade.play_sound(self.sound)

        if self.position_x < SCREEN_WIDTH - self.SQUARE_CENTER / 2:
            self.position_x = SCREEN_WIDTH- self.SQUARE_CENTER / 2
            arcade.play_sound(self.sound)

        if self.position_y < self.SQUARE_CENTER / 2:
            self.position_y = self.SQUARE_CENTER / 2
            arcade.play_sound(self.sound)

        if self.position_y < SCREEN_HEIGHT - self.SQUARE_CENTER/ 2:
            self.position_y = SCREEN_HEIGHT - self.SQUARE_CENTER / 2
            arcade.play_sound(self.sound)




class MyApplication(arcade.Window):

    def __init__(self, width, height, title):


        super().__init__(width, height, title)


        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE_GRAY)

        # Create our ball
        self.ball = Ball(50, 50, 0,0, 15, arcade.color.PALE_AQUA)

        #create the square
        self.square = Square(550,50,40,40,SQUARE_CENTER,arcade.color.PALE_AQUA)

        self.laser_sound = arcade.load_sound("laser(1).ogg")
    def animate(self, delta_time):
        self.ball.animate()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
    def on_draw(self):

        arcade.start_render()
        draw_sunset(800, 500)
        draw_ocean(50, 50)
        draw_whale(500, 200)
        self.ball.draw()
        self.square.draw()

    def on_mouse_motion(self, x, y, dx, dy):

        self.square.position_x = x
        self.square.position_y = y
    def on_mouse_press(self,x,y, button, modifiers):
        arcade.play_sound(self.laser_sound)





window = MyApplication(640, 480, "Lab #7")


arcade.run()