import pygame

WINDOW_SIZE = (1366, 768)
WINDOW_MODE_FLAGS = 0  # pygame.NOFRAME


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE, WINDOW_MODE_FLAGS)
        self.background_colour = (255, 100, 125)

        self.screen.fill(self.background_colour)
        pygame.display.set_caption("ChessAI")
        pygame.display.flip()

