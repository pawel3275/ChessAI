from window import Window, WINDOW_SIZE
from event import EventHandler
from main_menu import MainMenu
import pygame


if __name__ == '__main__':
    pygame.init()
    main_window = Window()
    menu_view = MainMenu()


    eventCode = 1
    while eventCode != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        menu_view.draw_buttons()
        pygame.display.update()
        pygame.display.flip()
