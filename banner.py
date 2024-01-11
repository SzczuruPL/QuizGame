import pygame


class Banner:
    def __init__(self, x, y, image, text):
        self.x = x
        self.y = y
        self.image = image
        self.text = text
        self.font_size = 36
        self.font = pygame.font.Font(None, self.font_size)
        self.text_color = (0, 0, 0)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        text_render = self.font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=(self.x + self.image.get_width() // 2, self.y + self.image.get_height() // 2))
        surface.blit(text_render, text_rect)

    def set_color(self, color):
        self.text_color = color

    def set_fontsize(self, font_size):
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)

    def set_text(self, text):
        self.text = text