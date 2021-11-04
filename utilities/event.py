import pygame


class EventHandler:
    mouse_button_code = 0
    window_code = 0

    def __init__(self):
        pass

    @staticmethod
    def process_event(event):
        EventHandler.mouse_button_code = EventHandler.__on_mouse_button_down(event)
        EventHandler.window_code = EventHandler.__on_window_action(event)

    @staticmethod
    def __on_window_action(event):
        if event.type == pygame.QUIT:
            return 2
        if event.type == pygame.RESIZABLE:
            pass

    @staticmethod
    def __on_mouse_button_down(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return 4
            elif event.button == 2:
                return 5
            elif event.button == 3:
                return 6
        return 0



