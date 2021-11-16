import pygame
import os
from views.view import View
from game.chess_context import ChessGameContext

IMG_PATH = "images/default_pieces_and_figures/"
CHESS_PIECE_SIZE = (64, 64)


class ChessGameView(View):
    def __init__(self):
        super().__init__()
        self.images = {}
        self.__load_images()
        self.__create_game_ontext()

    def __load_images(self):
        # Load pieces and figures as surfaces from image folder.
        for filename in os.listdir(IMG_PATH):
            image_name = os.path.splitext(filename)[0]
            self.images[image_name] = pygame.transform.scale(pygame.image.load(IMG_PATH + filename), CHESS_PIECE_SIZE)

    def __create_game_ontext(self):
        self.game_context = ChessGameContext()

    def __draw_board(self):
        white_color = pygame.Color("white")
        grey_color = pygame.Color("gray")

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = white_color
                else:
                    color = grey_color

                pygame.draw.rect(self.screen, color, pygame.Rect(j * 64, i * 64, 64, 64))

    def __draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.game_context.board[i][j]
                if piece != "__":
                    self.screen.blit(self.images[piece], pygame.Rect(j * 64, i * 64, 64, 64))

    def draw_view(self):
        self.__draw_board()
        self.__draw_pieces()
