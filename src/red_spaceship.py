from src.spaceship import Spaceship
import pygame

class RedSpaceship(Spaceship):
    """
    A class representing a red spaceship, derived from the Spaceship class.

    Attributes:
        Inherits attributes from the Spaceship class.

    Methods:
        __init__(self, pos_x, pos_y):
            Initializes a RedSpaceship object.

        handle_movement(self):
            Handles the movement of the red spaceship based on keyboard input.
    """

    def __init__(self, pos_x, pos_y):
        """
        Initializes a RedSpaceship object.

        Args:
            pos_x (int): The initial x-coordinate of the red spaceship.
            pos_y (int): The initial y-coordinate of the red spaceship.
        """
        super().__init__("assets/spaceship_red.png", 50, 50, pos_x, pos_y)

    def handle_movement(self):
        """
        Handles the movement of the red spaceship based on keyboard input.
        """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x - Spaceship.VELOCITY > 0:  # BACKWARD
            self.rect.x -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_d] and self.rect.x + Spaceship.VELOCITY + self.rect.width < Spaceship.BORDER.x:  # FORWARD
            self.rect.x += Spaceship.VELOCITY
        if keys_pressed[pygame.K_w] and self.rect.y - Spaceship.VELOCITY > 0:  # UPWARD
            self.rect.y -= Spaceship.VELOCITY
        if keys_pressed[pygame.K_s] and self.rect.y + Spaceship.VELOCITY + self.rect.height < Spaceship.HEIGHT:  # DOWNWARD
            self.rect.y += Spaceship.VELOCITY
