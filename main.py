from window import Window, WINDOW_SIZE
from event import EventHandler
from button import Button
import pygame


def main_menu_view(screen):
    horizontal_border_gap = 8
    vertical_border_gap = 8

    small_button_width = 250
    small_button_height = 100

    large_button_width = 250
    large_button_height = 200

    main_menu_buttons = []

    options_button_pos = ((WINDOW_SIZE[0] / 2) - (small_button_width / 2),  # horizontal position
                          (WINDOW_SIZE[1] / 2))  # vertical position

    quit_button_pos = ((WINDOW_SIZE[0] / 2) - (small_button_width / 2),  # horizontal position
                       (WINDOW_SIZE[1] / 2) + small_button_height + vertical_border_gap)  # vertical position

    play_reinforced_button_pos = ((WINDOW_SIZE[0] / 2) - (small_button_width / 2),  # horizontal position
                                  (WINDOW_SIZE[1] / 2) - vertical_border_gap - large_button_height)  # vertical position

    play_dense_button_pos = ((play_reinforced_button_pos[0] - horizontal_border_gap - large_button_width),
                             play_reinforced_button_pos[1])

    play_multiplayer_button_pos = ((play_reinforced_button_pos[0] + horizontal_border_gap + large_button_width),
                                   play_reinforced_button_pos[1])

    quit_button = Button(screen, (quit_button_pos[0], quit_button_pos[1], small_button_width, small_button_height),
                         "QUIT")
    main_menu_buttons.append(quit_button)

    options_button = Button(screen,
                            (options_button_pos[0], options_button_pos[1], small_button_width, small_button_height),
                            "OPTIONS")
    main_menu_buttons.append(options_button)

    play_reinforced_button = Button(screen,
                                    (play_reinforced_button_pos[0], play_reinforced_button_pos[1], large_button_width,
                                     large_button_height), "REINFORCED")
    main_menu_buttons.append(play_reinforced_button)

    play_dense_button = Button(screen,
                               (play_dense_button_pos[0], play_dense_button_pos[1], large_button_width,
                                large_button_height), "DENSE")
    main_menu_buttons.append(play_dense_button)

    play_multiplayer_button = Button(screen,
                                     (
                                     play_multiplayer_button_pos[0], play_multiplayer_button_pos[1], large_button_width,
                                     large_button_height),
                                     "MULTIPLAYER")
    main_menu_buttons.append(play_multiplayer_button)

    for button in main_menu_buttons:
        button.draw_button()


if __name__ == '__main__':
    is_game_running = True
    main_window = Window()
    eventCode = 1
    pygame.init()

    while eventCode != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        main_menu_view(main_window.screen)
        pygame.display.update()
        pygame.display.flip()
