import pygame


class Button:
    def __init__(self, screen, size, text, box_color=(50, 255, 255), text_color=(10, 100, 10), font='arial',
                 font_size=35):
        self.screen = screen
        self.box_color = box_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        self.rect = pygame.Rect(size)

    def add_rect(self):
        pygame.draw.rect(self.screen, self.box_color, self.rect)

    def add_text(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_scale_width = (self.rect[2] / len(self.text)) *1.55
        text_scale_height = self.rect[3] / 3.2
        text_position = (self.rect[0] + text_scale_width, self.rect[1] + text_scale_height)
        self.screen.blit(text_surface, text_position)

    def draw_button(self):
        self.add_rect()
        self.add_text()
        pygame.display.update()
