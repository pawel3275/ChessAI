import pygame
import sys

class Button:
    def __init__(self, size, text, color=(50, 255, 255), font='arial', font_size=35):
        self.color = color
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = pygame.Rect(size)

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
