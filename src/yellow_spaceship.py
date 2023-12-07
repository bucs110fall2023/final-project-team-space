from src.spaceship import Spaceship
import pygame


class YellowSpaceship(Spaceship):
    def __init__(self, pos_x, pos_y):
        super().__init__("assets/spaceship_yellow.png", 50, 50, pos_x, pos_y)
        rotated_img = pygame.transform.rotate(self.image, 180)
        self.image = rotated_img

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x - Spaceship.VELOCITY > Spaceship.BORDER.x + Spaceship.BORDER.width:  # BACKWARD
            self.rect.x -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_RIGHT] and self.rect.x + Spaceship.VELOCITY + self.rect.width < Spaceship.WIDTH:  # FORWARD
            self.rect.x += Spaceship.VELOCITY
        if keys_pressed[pygame.K_UP] and self.rect.y - Spaceship.VELOCITY > 0:  # UPWARD
            self.rect.y -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_DOWN] and self.rect.y + Spaceship.VELOCITY + self.rect.height < Spaceship.HEIGHT:  # DOWNWARD
            self.rect.y += Spaceship.VELOCITY
