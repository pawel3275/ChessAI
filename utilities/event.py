import pygame


class EventHandler:
    def __init__(self):
        pass

    @staticmethod
    def process_event(event):
        if event.type == pygame.QUIT:
            return 2
        if event.type == pygame.RESIZABLE:
            return 3

    @staticmethod
    def on_button_click():
        pass

