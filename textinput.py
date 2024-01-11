import pygame


class TextInput:
    def __init__(self, x, y, images, default_text):
        width = images["normal"].get_width()
        height = images["normal"].get_height()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = images
        self.default_text = default_text
        self.text = default_text
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self.state = "normal"
        self.color = (128, 128, 128)
        self.has_input = False

    def draw(self, surface):
        if self.state == "normal":
            surface.blit(self.images["normal"], (self.x, self.y))
        elif self.state == "active":
            surface.blit(self.images["active"], (self.x, self.y))

        text_render = self.font.render(self.text, True, self.color)
        text_rect = text_render.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text_render, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.state = "active"
            else:
                self.state = "normal"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.state = "active"
                if not self.has_input:
                    self.text = ""
                    self.color = (0, 0, 0)
                    self.has_input = True
            else:
                self.state = "normal"
        elif event.type == pygame.KEYDOWN:
            if self.state == "active":
                if not self.has_input:
                    self.text = ""
                    self.color = (0, 0, 0)
                    self.has_input = True
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.state = "normal"
                else:
                    self.text += event.unicode

    def get_text(self):
        return self.text
