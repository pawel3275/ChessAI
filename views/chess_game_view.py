import os
from views.window import Window, WINDOW_SIZE, BORDER_GAP, DEFAULT_BACKGROUND_COLOR
from game.chess_context import ChessGameContext
from utilities.button import Button, SMALL_BUTTON_SIZE, ON_BUTTON_COLLISION_COLOR, DEFAULT_BUTTON_COLOR
from utilities.event import EventHandler
from game.move import Move
import pygame

IMG_PATH = "images/default_pieces_and_figures/"
CHESS_PIECE_SIZE = (64, 64)
TILE_SIZE = (64, 64)
BORDER_OFFSET = (128, 128)  # Change to ((WINDOWSIZE - TILE_SIZE[0] * 8) / 2), ... )


class ChessGameView(Window):
    def __init__(self):
        super().__init__()
        self.images = {}
        self.board_rects = []
        self.square_selected = ()
        self.player_clicks = []
        self.move_made = False
        self.__load_images()
        self.__create_game_ontext()
        self.__calculate_rect_positions()
        self.__create_button_rect_list(self.screen)

    def __load_images(self):
        # Load pieces and figures as surfaces from image folder.
        for filename in os.listdir(IMG_PATH):
            image_name = os.path.splitext(filename)[0]
            self.images[image_name] = pygame.transform.scale(pygame.image.load(IMG_PATH + filename), CHESS_PIECE_SIZE)

    def __create_game_ontext(self):
        self.game_context = ChessGameContext()
        self.valid_moves = self.game_context.get_valid_moves()

    def __draw_board(self):
        white_color = pygame.Color("white")
        grey_color = pygame.Color("gray")

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = white_color
                else:
                    color = grey_color

                board_rect = pygame.Rect(j * TILE_SIZE[0] + BORDER_OFFSET[0], i * TILE_SIZE[1] + BORDER_OFFSET[1],
                                             TILE_SIZE[0], TILE_SIZE[1])

                self.board_rects.append(board_rect)
                pygame.draw.rect(self.screen, color, board_rect)

    def __draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.game_context.board[i][j]
                if piece != "__":
                    rect = pygame.Rect(j * TILE_SIZE[0] + BORDER_OFFSET[0], i * TILE_SIZE[1]+ BORDER_OFFSET[1], CHESS_PIECE_SIZE[0], CHESS_PIECE_SIZE[1])
                    self.screen.blit(self.images[piece], rect)

    def __calculate_rect_positions(self):
        middle_point = (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)

        grid_horizontal_left_lane = BORDER_OFFSET[0]
        grid_horizontal_middle_lane = BORDER_OFFSET[0] + TILE_SIZE[0] * 8 + BORDER_GAP
        grid_horizontal_right_lane = WINDOW_SIZE[0] - BORDER_OFFSET[0]

        grid_vertical_top_lane = BORDER_OFFSET[1]
        grid_vertical_middle_lane = BORDER_OFFSET[1] + (TILE_SIZE[1] * 8) / 3  # TODO remove / 3 later
        grid_vertical_bottom_lane = WINDOW_SIZE[1] - BORDER_OFFSET[1]

        self.back_button_pos = (grid_horizontal_middle_lane, grid_vertical_middle_lane)

    def __create_button_rect_list(self, screen):
        rect_position = (self.back_button_pos, SMALL_BUTTON_SIZE)
        self.window_buttons.append(Button(screen, "id_back_button", rect_position, "BACK"))

    def __check_button_mouse_collision(self):
        mouse_pointer_pos = pygame.mouse.get_pos()
        for button in self.window_buttons:
            if button.rect.collidepoint(mouse_pointer_pos):
                button.box_color = ON_BUTTON_COLLISION_COLOR
                if button.id == "id_back_button" and EventHandler.mouse_button_code == 4:
                    EventHandler.on_view_change(0)
            else:
                button.box_color = DEFAULT_BUTTON_COLOR

    def reset_view(self):
        self.background_colour = DEFAULT_BACKGROUND_COLOR
        self.screen.fill(self.background_colour)

    def draw_view(self):
        self.__draw_board()
        self.__draw_pieces()
        self.__check_button_mouse_collision()
        for button in self.window_buttons:
            button.draw_button()

