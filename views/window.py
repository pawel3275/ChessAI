import pygame

WINDOW_SIZE = (1366, 768)
WINDOW_MODE_FLAGS = 0
MAX_FPS = 30
SMALL_BUTTON_SIZE = [250, 100]
LARGE_BUTTON_SIZE = [250, 200]
BORDER_GAP = 8
ON_BUTTON_COLLISION_COLOR = (255, 0, 0)
DEFAULT_BUTTON_COLOR = (50, 255, 255)
DEFAULT_BUTTON_TEXT_COLOR = (10, 100, 10)
DEFAULT_BACKGROUND_COLOR = (255, 100, 125)


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE, WINDOW_MODE_FLAGS)
        self.background_colour = DEFAULT_BACKGROUND_COLOR

        self.screen.fill(self.background_colour)
        pygame.display.set_caption("ChessAI")
        pygame.display.flip()

