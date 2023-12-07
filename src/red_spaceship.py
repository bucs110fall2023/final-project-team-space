from src.spaceship import Spaceship
import pygame

class RedSpaceship(Spaceship):
    def __init__(self, pos_x, pos_y):
        super().__init__("assets/spaceship_red.png", 50, 50, pos_x, pos_y)

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x - Spaceship.VELOCITY > 0:  # BACKWARD
            self.rect.x -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_d] and self.rect.x + Spaceship.VELOCITY + self.rect.width < Spaceship.BORDER.x:  # FORWARD
            self.rect.x += Spaceship.VELOCITY
        if keys_pressed[pygame.K_w] and self.rect.y - Spaceship.VELOCITY > 0:  # UPWARD
            self.rect.y -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_s] and self.rect.y + Spaceship.VELOCITY + self.rect.height < Spaceship.HEIGHT:  # DOWNWARD
            self.rect.y += Spaceship.VELOCITY
