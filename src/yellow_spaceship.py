from src.spaceship import Spaceship
import pygame


class YellowSpaceship(Spaceship):
    """
    A class representing a yellow spaceship, derived from the Spaceship class.

    Attributes:
        Inherits attributes from the Spaceship class.

    Methods:
        __init__(self, pos_x, pos_y):
            Initializes a YellowSpaceship object.

        handle_movement(self):
            Handles the movement of the yellow spaceship based on keyboard input.
    """
    
    def __init__(self, pos_x, pos_y):
        """
        Initializes a YellowSpaceship object.

        Args:
            pos_x (int): The initial x-coordinate of the yellow spaceship.
            pos_y (int): The initial y-coordinate of the yellow spaceship.
        """
        super().__init__("assets/spaceship_yellow.png", 50, 50, pos_x, pos_y)
        rotated_img = pygame.transform.rotate(self.image, 180)
        self.image = rotated_img

    def handle_movement(self):
        """
        Handles the movement of the yellow spaceship based on keyboard input.
        """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x - Spaceship.VELOCITY > Spaceship.BORDER.x + Spaceship.BORDER.width:  # BACKWARD
            self.rect.x -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_RIGHT] and self.rect.x + Spaceship.VELOCITY + self.rect.width < Spaceship.WIDTH:  # FORWARD
            self.rect.x += Spaceship.VELOCITY
        if keys_pressed[pygame.K_UP] and self.rect.y - Spaceship.VELOCITY > 0:  # UPWARD
            self.rect.y -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_DOWN] and self.rect.y + Spaceship.VELOCITY + self.rect.height < Spaceship.HEIGHT:  # DOWNWARD
            self.rect.y += Spaceship.VELOCITY
