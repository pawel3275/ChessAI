import pygame
import os

IMG_PATH = "images/default_pieces_and_figures/"
CHESS_PIECE_SIZE = (32, 32)


class ChessEngine:
    def __init__(self):
        self.player_to_move = 0
        self.images = {}

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

                pygame.draw.rect(screen, color, pygame.Rect(j * 8, i * 8, 8, 8))

    def draw_pieces(self, screen, board):
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != "__":
                    screen.blit(self.images[piece], pygame.Rect(j * 8, i * 8, 8, 8))
