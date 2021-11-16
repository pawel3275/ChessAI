from views.window import *
import pygame


class View(Window):
    def __init__(self):
        super().__init__()
        self.view_buttons = []
        self.current_view = None

    def draw_view(self, view):
        self.current_view = view
        view.draw_view()
        pygame.display.update()

