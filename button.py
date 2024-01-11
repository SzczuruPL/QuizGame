import pygame


class Button:
    def __init__(self, x, y, images, text, font_size=24):
        width = images["normal"].get_width()
        height = images["normal"].get_height()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = images
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self.state = "normal"
        self.color = (255, 255, 255)

    def draw(self, surface):
        if self.state == "normal":
            surface.blit(self.images["normal"], (self.x, self.y))
        elif self.state == "hover":
            surface.blit(self.images["hover"], (self.x, self.y))
        elif self.state == "click":
            surface.blit(self.images["click"], (self.x, self.y))

        text_render = self.font.render(self.text, True, self.color)
        text_rect = text_render.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text_render, text_rect)

    def set_color(self, color):
        self.color = color

    def set_text(self, text):
        self.text = text

    def set_fontsize(self, font_size):
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.state = "hover"
            else:
                self.state = "normal"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.state = "click"
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.state == "click":
                self.state = "hover"
                return True

        return False
