from views.window import MAX_FPS
from utilities.event import EventHandler
from views.main_menu_view import MainMenuView
from views.view import View
import pygame
from views.chess_game_view import ChessGameView


def draw_game_state(screen, game_state):
    game_state.draw_board(screen)
    game_state.draw_pieces(screen, game_state.board)


if __name__ == '__main__':
    pygame.init()
    game_view = View()
    menu_view = MainMenuView()
    gameEngine = ChessGameView()
    clock = pygame.time.Clock()

    while EventHandler.window_code != 2:
        # Event processing
        for event in pygame.event.get():
            eventCode = EventHandler.process_event(event)

        #game_view.draw_view(gameEngine)
        game_view.draw_view(menu_view)

        clock.tick(MAX_FPS)
        pygame.display.flip()
