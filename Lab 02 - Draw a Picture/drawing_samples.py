import arcade

HEIGHT = 600
WIDTH = 800
TITLE_WINDOW = 'Test'


def main():
    arcade.open_window(WIDTH, HEIGHT, TITLE_WINDOW)
    arcade.set_background_color(arcade.csscolor.AQUAMARINE)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.DARK_GREEN)
    # Draw rectangle tree
    arcade.draw_lrtb_rectangle_filled(100, 120, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_lrtb_rectangle_filled(50, 170, 500, 400, arcade.csscolor.DARK_GREEN)  # Draw rectangle crown of tree
    # Draw circle tree
    arcade.draw_lrtb_rectangle_filled(240, 260, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_circle_filled(250, 450, 50, arcade.csscolor.DARK_GREEN)  # Draw circle crown of tree
    # Draw ellipse tree
    arcade.draw_lrtb_rectangle_filled(360, 380, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_ellipse_filled(370, 470, 100, 150, arcade.csscolor.DARK_GREEN)  # Draw ellipse crown of tree
    # Draw arc tree
    arcade.draw_lrtb_rectangle_filled(480, 500, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_arc_filled(490, 400, 100, 150, arcade.csscolor.DARK_GREEN, 0, 180)  # Draw arc crown of tree
    # Draw triangle tree
    arcade.draw_lrtb_rectangle_filled(600, 620, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_triangle_filled(610, 500, 550, 350, 670, 350, arcade.csscolor.DARK_GREEN)  # Draw triangle crown of tree
    # Draw polygonal tree
    arcade.draw_lrtb_rectangle_filled(720, 740, 400, 300, arcade.csscolor.BROWN)  # Draw trunk of tree
    arcade.draw_polygon_filled(((730, 500),
                                (710, 470),
                                (700, 400),
                                (760, 400),
                                (750, 470)),
                               arcade.csscolor.DARK_GREEN)  # Draw polygonal crown of tree
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()
