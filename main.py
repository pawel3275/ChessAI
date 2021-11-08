from utilities.window import Window, MAX_FPS
from utilities.event import EventHandler
from menu.main_menu import MainMenu
import pygame
from game.chess_engine import ChessEngine


def draw_game_state(screen, game_state):
    game_state.draw_board(screen)
    game_state.draw_pieces(screen, game_state.board)


if __name__ == '__main__':
    pygame.init()
    main_window = Window()
    menu_view = MainMenu()
    clock = pygame.time.Clock()

    while EventHandler.window_code != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        menu_view.draw_buttons()
        pygame.display.update()

        test = ChessEngine()
        test.load_images()

        clock.tick(MAX_FPS)
        pygame.display.flip()
