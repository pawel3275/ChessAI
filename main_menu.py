from window import Window, WINDOW_SIZE
from button import Button
import pygame


class MainMenu(Window):
    def __init__(self):
        super().__init__()
        self.buttons = []

        self.horizontal_border_gap = 8
        self.vertical_border_gap = 8
        self.small_button_width = 250
        self.small_button_height = 100
        self.large_button_width = 250
        self.large_button_height = 200
        self.options_button_pos = None
        self.play_multiplayer_button_pos = None
        self.quit_button_pos = None
        self.play_reinforced_button_pos = None
        self.play_dense_button_pos = None

        self.__calculate_rect_positions()
        self.__create_button_rect_list(self.screen)

    def __calculate_rect_positions(self):
        self.options_button_pos = ((WINDOW_SIZE[0] / 2) - (self.small_button_width / 2), (WINDOW_SIZE[1] / 2))

        self.quit_button_pos = ((WINDOW_SIZE[0] / 2) - (self.small_button_width / 2),
                                (WINDOW_SIZE[1] / 2) + self.small_button_height + self.vertical_border_gap)

        self.play_reinforced_button_pos = ((WINDOW_SIZE[0] / 2) - (self.small_button_width / 2), (
                WINDOW_SIZE[1] / 2) - self.vertical_border_gap - self.large_button_height)

        self.play_dense_button_pos = (
            (self.play_reinforced_button_pos[0] - self.horizontal_border_gap - self.large_button_width),
            self.play_reinforced_button_pos[1])

        self.play_multiplayer_button_pos = (
            (self.play_reinforced_button_pos[0] + self.horizontal_border_gap + self.large_button_width),
            self.play_reinforced_button_pos[1])

    def __create_button_rect_list(self, screen):
        quit_button = Button(screen, (
            self.quit_button_pos[0], self.quit_button_pos[1], self.small_button_width, self.small_button_height),
                             "QUIT")
        self.buttons.append(quit_button)

        options_button = Button(screen,
                                (self.options_button_pos[0], self.options_button_pos[1], self.small_button_width,
                                 self.small_button_height),
                                "OPTIONS")
        self.buttons.append(options_button)

        play_reinforced_button = Button(screen,
                                        (self.play_reinforced_button_pos[0], self.play_reinforced_button_pos[1],
                                         self.large_button_width,
                                         self.large_button_height), "REINFORCED")
        self.buttons.append(play_reinforced_button)

        play_dense_button = Button(screen,
                                   (self.play_dense_button_pos[0], self.play_dense_button_pos[1],
                                    self.large_button_width,
                                    self.large_button_height), "DENSE")
        self.buttons.append(play_dense_button)

        play_multiplayer_button = Button(screen,
                                         (
                                             self.play_multiplayer_button_pos[0], self.play_multiplayer_button_pos[1],
                                             self.large_button_width,
                                             self.large_button_height),
                                         "MULTIPLAYER")
        self.buttons.append(play_multiplayer_button)

    def __check_button_mouse_collision(self):
        mouse_pointer_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pointer_pos):
                button.box_color = (255, 0, 0)
            else:
                button.box_color = (50, 255, 255)

    def draw_buttons(self):
        self.__check_button_mouse_collision()

        for button in self.buttons:
            button.draw_button()
            pygame.display.flip()







