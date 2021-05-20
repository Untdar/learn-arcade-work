import arcade

HEIGHT = 600
WIDTH = 600
TITLE_WINDOW = 'Test'


def main():
    arcade.open_window(WIDTH, HEIGHT, TITLE_WINDOW)
    arcade.set_background_color(arcade.csscolor.AQUA)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()
