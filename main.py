from views.window import MAX_FPS
from utilities.event import EventHandler
from views.window import Window
from views.view_handler import ViewHandler
import pygame


if __name__ == '__main__':
    pygame.init()
    game_main_window = Window()
    game_view = ViewHandler()
    clock = pygame.time.Clock()

    while EventHandler.window_code != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        game_view.draw_view()

        clock.tick(MAX_FPS)
        pygame.display.flip()
