from utilities.window import Window
from utilities.event import EventHandler
from menu.main_menu import MainMenu
import pygame


if __name__ == '__main__':
    pygame.init()
    main_window = Window()
    menu_view = MainMenu()

    while EventHandler.window_code != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        menu_view.draw_buttons()
        pygame.display.update()
        pygame.display.flip()
