import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 45:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 50:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 10:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT - 40:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
