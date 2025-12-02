import pygame


class Player:
    def __init__(self, x, y):
        self.width = 80
        self.height = 60
        self.x = x
        self.y = y
        self.speed = 8
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def update(self, screen_width):
        if self.x < self.width // 2:
            self.x = self.width // 2
        if self.x > screen_width - self.width // 2:
            self.x = screen_width - self.width // 2

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (139, 69, 19), self.rect, border_radius=10)
        pygame.draw.rect(screen, (160, 82, 45), self.rect, 3, border_radius=10)