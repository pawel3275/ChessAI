import pygame
import os
from menu.view import View
import numpy as np

IMG_PATH = "images/default_pieces_and_figures/"
CHESS_PIECE_SIZE = (64, 64)


class ChessEngine(View):
    def __init__(self):
        super().__init__()
        self.player_to_move = 0

        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"],
        ])

        self.moveLog = []

        self.images = {}
        self.load_images()

    def load_images(self):
        # Load pieces and figures as surfaces from image folder.
        for filename in os.listdir(IMG_PATH):
            self.images[os.path.splitext(filename)[0]] = pygame.transform.scale(pygame.image.load(IMG_PATH + filename),
                                                                                CHESS_PIECE_SIZE)

    def draw_board(self, screen):
        white_color = pygame.Color("white")
        grey_color = pygame.Color("gray")

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = white_color
                else:
                    color = grey_color

                pygame.draw.rect(screen, color, pygame.Rect(j * 64, i * 64, 64, 64))

    def draw_pieces(self, screen, board):
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != "__":
                    screen.blit(self.images[piece], pygame.Rect(j * 64, i * 64, 64, 64))

    def draw_view(self):
        self.draw_board(self.screen)
        self.draw_pieces(self.screen, self.board)
