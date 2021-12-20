import pygame
from game.move import Move

TILE_SIZE = (64, 64)
BORDER_OFFSET = (128, 128)
EVENT_CODES = {
    0: "SUCCESS",
    1: "RUNNING",
    2: "GAME_QUIT",
    3: "ERROR",
    4: "LEFT_MOUSE_BUTTON_PRESSED",
    5: "RIGHT_MOUSE_BUTTON_PRESSED",
    6: "MIDDLE_MOUSE_BUTTON_PRESSED",
    7: "DENSE_PLAY",
    8: "MAIN_MENU"
}


class EventHandler:
    mouse_button_code = 0
    window_code = 0
    view_code = 0

    @staticmethod
    def process_event(event):
        EventHandler.mouse_button_code = EventHandler.on_mouse_button_down(event)
        EventHandler.window_code = EventHandler.on_window_action(event)

    @staticmethod
    def on_view_change(new_view):
        EventHandler.view_code = new_view

    @staticmethod
    def on_window_action(event):
        if event.type == pygame.QUIT:
            return 2
        if event.type == pygame.RESIZABLE:
            pass

    @staticmethod
    def mouse_board_process(event, game_view):
        if EventHandler.view_code == 1:
            current_view = game_view.current_view
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                row = (location[1] - BORDER_OFFSET[1]) // 64
                col = (location[0] - BORDER_OFFSET[0]) // 64
                if current_view.square_selected == (row, col):
                    current_view.square_selected = ()
                    current_view.player_clicks = []
                else:
                    current_view.square_selected = (row, col)
                    current_view.player_clicks.append(current_view.square_selected)
                if len(current_view.player_clicks) == 2:
                    move = Move(current_view.player_clicks[0], current_view.player_clicks[1], current_view.game_context.board)
                    print(move.get_chess_notation())
                    if move in current_view.valid_moves:
                        current_view.game_context.make_move(move)
                        current_view.move_made = True
                        current_view.square_selected = ()
                        current_view.player_clicks = []
                    else:
                        current_view.player_clicks = [current_view.square_selected]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_view.game_context.undo_move()
                    current_view.move_made = True

            if current_view.move_made:
                current_view.valid_moves = current_view.game_context.get_valid_moves()
                current_view.move_made = False

    @staticmethod
    def on_mouse_button_down(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return 4
            elif event.button == 2:
                return 5
            elif event.button == 3:
                return 6
        return 0



