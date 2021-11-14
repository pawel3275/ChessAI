from utilities.window import Window
import pygame


class View(Window):
    def __init__(self):
        super().__init__()
        self.current_view = None

    def draw_view(self, view):
        self.current_view = view
        view.draw_view()
        pygame.display.update()

