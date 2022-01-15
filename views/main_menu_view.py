from utilities.button import Button, SMALL_BUTTON_SIZE, LARGE_BUTTON_SIZE, ON_BUTTON_COLLISION_COLOR, DEFAULT_BUTTON_COLOR
from utilities.event import EventHandler
from views.window import *
import pygame

BACKGROUND_PATH = "images/"


class MainMenuView(Window):
    def __init__(self):
        super().__init__()
        self.__calculate_rect_positions()
        self.__create_button_rect_list(self.screen)
        self.limited_draws = False

    '''
        Loads the image to backgrounds and blits the screen to show it
    '''
    def __set_background(self):
        background = pygame.image.load(BACKGROUND_PATH + "menu_background.jpg")
        self.screen.blit(background, (0, 0))
        self.limited_draws = True

    '''
        Populates grid variables for buttons regarding their positions
    '''
    def __calculate_rect_positions(self):
        middle_point = (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)

        grid_horizontal_left_lane = middle_point[0] - (SMALL_BUTTON_SIZE[0] / 2) - BORDER_GAP - LARGE_BUTTON_SIZE[0]
        grid_horizontal_middle_lane = middle_point[0] - (SMALL_BUTTON_SIZE[0] / 2)
        grid_horizontal_right_lane = middle_point[0] - (SMALL_BUTTON_SIZE[0] / 2) + BORDER_GAP + LARGE_BUTTON_SIZE[0]

        grid_vertical_top_lane = middle_point[1] - LARGE_BUTTON_SIZE[1] - BORDER_GAP
        grid_vertical_middle_lane = middle_point[1]
        grid_vertical_bottom_lane = middle_point[1] + SMALL_BUTTON_SIZE[1] + BORDER_GAP

        self.options_button_pos = (grid_horizontal_middle_lane, grid_vertical_middle_lane)
        self.quit_button_pos = (grid_horizontal_middle_lane, grid_vertical_bottom_lane)
        self.play_reinforced_button_pos = (grid_horizontal_middle_lane, grid_vertical_top_lane)
        self.play_dense_button_pos = (grid_horizontal_left_lane, grid_vertical_top_lane)
        self.play_multiplayer_button_pos = (grid_horizontal_right_lane, grid_vertical_top_lane)

    '''
        Populates rectangle button list for the given view
    '''
    def __create_button_rect_list(self, screen):
        rect_position = (self.quit_button_pos, SMALL_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_quit_button", rect_position, "QUIT"))

        rect_position = (self.options_button_pos, SMALL_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_options_button", rect_position, "OPTIONS"))

        rect_position = (self.play_reinforced_button_pos, LARGE_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_reinforced_game", rect_position, "REINFORCED"))

        rect_position = (self.play_dense_button_pos, LARGE_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_dense_game", rect_position, "DENSE"))

        rect_position = (self.play_multiplayer_button_pos, LARGE_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_multiplayer_game", rect_position, "MULTIPLAYER"))

    '''
        Checks if the mouse button is on collision with a rect
    '''
    def __check_button_mouse_collision(self):
        mouse_pointer_pos = pygame.mouse.get_pos()
        for button in self.window_buttons:
            if button.rect.collidepoint(mouse_pointer_pos):
                button.box_color = ON_BUTTON_COLLISION_COLOR
                if button.id == "id_quit_button" and EventHandler.mouse_button_code == 4:
                    EventHandler.window_code = 2
                elif button.id == "id_dense_game" and EventHandler.mouse_button_code == 4:
                    EventHandler.on_view_change(1)
            else:
                button.box_color = DEFAULT_BUTTON_COLOR

    '''
        Draws the buttons for the current view stacked in the class button list
    '''
    def draw_buttons(self):
        self.__check_button_mouse_collision()
        for button in self.window_buttons:
            button.draw_button()

    '''
        Resets the whole view to the default background color
    '''
    def reset_view(self):
        self.background_colour = DEFAULT_BACKGROUND_COLOR
        self.screen.fill(self.background_colour)

    '''
        Draws the whole view consisting on background, buttons etc.
    '''
    def draw_view(self):
        if not self.limited_draws:
            self.__set_background()
        self.draw_buttons()
