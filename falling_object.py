import pygame


class FallingObject:
    def __init__(self, x, y, obj_type, speed):
        self.x = x
        self.y = y
        self.obj_type = obj_type
        self.speed = speed

        if obj_type == "apple":
            self.color = (255, 0, 0)
            self.radius = 15
        else:
            self.color = (100, 100, 100)
            self.radius = 15

        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (self.x, self.y)

    def update(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if self.obj_type == "apple":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            pygame.draw.circle(screen, (0, 100, 0), (self.x, self.y - 10), 5)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            pygame.draw.circle(screen, (70, 70, 70), (self.x, self.y), self.radius, 2)