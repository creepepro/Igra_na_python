import pygame
import random
from player import Player
from falling_object import FallingObject


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Яблокопад")

        self.clock = pygame.time.Clock()
        self.player = Player(self.width // 2, self.height - 50)

        self.falling_objects = []
        self.spawn_timer = 0
        self.spawn_delay = 30

        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font(None, 36)

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.__init__()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

        return True

    def spawn_objects(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0

            x = random.randint(20, self.width - 20)
            speed = random.uniform(2, 4)

            if random.random() < 0.7:
                obj_type = "apple"
            else:
                obj_type = "stone"

            obj = FallingObject(x, -20, obj_type, speed)
            self.falling_objects.append(obj)

    def update(self):
        if self.game_over:
            return

        self.player.update(self.width)
        self.spawn_objects()

        for obj in self.falling_objects[:]:
            obj.update()

            if obj.y > self.height:
                self.falling_objects.remove(obj)
                if obj.obj_type == "apple":
                    self.lives -= 1
            elif self.player.rect.colliderect(obj.rect):
                self.falling_objects.remove(obj)
                if obj.obj_type == "apple":
                    self.score += 1
                else:
                    self.lives -= 1

        if self.lives <= 0:
            self.game_over = True

    def draw(self):
        self.screen.fill((135, 206, 235))

        for obj in self.falling_objects:
            obj.draw(self.screen)

        self.player.draw(self.screen)

        score_text = self.font.render(f"Очки: {self.score}", True, (0, 0, 0))
        lives_text = self.font.render(f"Жизни: {self.lives}", True, (0, 0, 0))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

        if self.game_over:
            game_over_text = self.font.render("Игра окончена! Нажми R для перезапуска", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)