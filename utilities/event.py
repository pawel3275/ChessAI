import pygame

EVENT_CODES = {
    0: "SUCCESS",
    1: "RUNNING",
    2: "GAME_QUIT",
    3: "ERROR",
    4: "LEFT_MOUSE_BUTTON_PRESSED",
    5: "RIGHT_MOUSE_BUTTON_PRESSED",
    6: "MIDDLE_MOUSE_BUTTON_PRESSED",
    7: "DENSE_PLAY",
    8: "MAIN_MENU"
}


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



