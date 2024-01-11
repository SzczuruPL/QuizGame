import pygame

from banner import Banner


class DualBanner(Banner):
    def __init__(self, x, y, image, left_text, right_text):
        super().__init__(x, y, image, "")
        self.font_size = 36
        self.font = pygame.font.Font(None, self.font_size)
        self.left_text = left_text
        self.right_text = right_text
        self.text_color = (255, 255, 255)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        text_render_left = self.font.render(self.left_text, True, self.text_color)
        text_render_right = self.font.render(self.right_text, True, self.text_color)
        text_rect_left = text_render_left.get_rect(midleft=(self.x + 10, self.y + self.image.get_height() // 2))
        text_rect_right = text_render_right.get_rect(midright=(self.x + self.image.get_width() - 10, self.y + self.image.get_height() // 2))
        surface.blit(text_render_left, text_rect_left)
        surface.blit(text_render_right, text_rect_right)

    def set_color(self, color):
        self.text_color = color

