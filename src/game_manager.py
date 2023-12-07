import pygame
from src.spaceship import Spaceship

class GameManager:
    def __init__(self):
        self.BULLET_VELOCITY = 10
        self.MAX_BULLETS = 4
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.YELLOW_HIT = pygame.USEREVENT + 1
        self.RED_HIT = pygame.USEREVENT + 2

        self.red_bullets = []
        self.yellow_bullets = []

    def handle_bullets(self, yellow, red):
        for bullet in self.red_bullets:
            bullet.x += self.BULLET_VELOCITY
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.YELLOW_HIT))
                self.red_bullets.remove(bullet)
            elif bullet.x > Spaceship.WIDTH:
                self.red_bullets.remove(bullet)

        for bullet in self.yellow_bullets:
            bullet.x -= self.BULLET_VELOCITY
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.RED_HIT))
                self.yellow_bullets.remove(bullet)
            elif bullet.x < 0:
                self.yellow_bullets.remove(bullet)

    def draw_window(self, win):
        for bullet in self.red_bullets:
            pygame.draw.rect(win, self.RED, bullet)

        for bullet in self.yellow_bullets:
            pygame.draw.rect(win, self.YELLOW, bullet)
