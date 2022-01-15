import pygame
from views.main_menu_view import MainMenuView
from views.chess_game_view import ChessGameView
from utilities.event import EventHandler


class ViewHandler:
    def __init__(self):
        self.current_view = self.create_main_menu_view()
        self.current_view_index = 0

    @staticmethod
    def create_main_menu_view():
        return MainMenuView()

    @staticmethod
    def create_dense_main_menu_view():
        return ChessGameView()

    def draw_view(self):
        if self.current_view_index != EventHandler.view_code:
            if EventHandler.view_code == 0:  # main menu
                self.current_view = self.create_main_menu_view()
            if EventHandler.view_code == 1: #dense gampeplay
                self.current_view = self.create_dense_main_menu_view()
            self.current_view_index = EventHandler.view_code
            self.current_view.reset_view()

        self.current_view.draw_view()
        pygame.display.update()

