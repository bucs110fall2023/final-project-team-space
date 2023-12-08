import pygame
from src.spaceship import Spaceship

class GameManager:
    """
    A class representing a game manager for handling bullets and drawing the game window.

    Attributes:
        BULLET_VELOCITY (int): The velocity of bullets.
        MAX_BULLETS (int): The maximum number of bullets allowed.
        RED (tuple): The RGB color tuple for the red bullets.
        YELLOW (tuple): The RGB color tuple for the yellow bullets.
        YELLOW_HIT (int): The custom event for a hit on the yellow spaceship.
        RED_HIT (int): The custom event for a hit on the red spaceship.
        red_bullets (list): A list to store the red bullets.
        yellow_bullets (list): A list to store the yellow bullets.

    Methods:
        __init__(self):
            Initializes a GameManager object.

        handle_bullets(self, yellow, red):
            Handles the movement and collision detection of bullets.

        draw_window(self, win):
            Draws the game window with bullets.

    """

    def __init__(self):
        """
        Initializes a GameManager object.
        """
        self.BULLET_VELOCITY = 10
        self.MAX_BULLETS = 4
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.YELLOW_HIT = pygame.USEREVENT + 1
        self.RED_HIT = pygame.USEREVENT + 2

        self.red_bullets = []
        self.yellow_bullets = []

    def handle_bullets(self, yellow, red):
        """
        Handles the movement and collision detection of bullets.

        Args:
            yellow (pygame.Rect): The rectangle representing the yellow spaceship.
            red (pygame.Rect): The rectangle representing the red spaceship.
        """
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
        """
        Draws the game window with bullets.

        Args:
            win (pygame.Surface): The game window surface.
        """
        for bullet in self.red_bullets:
            pygame.draw.rect(win, self.RED, bullet)

        for bullet in self.yellow_bullets:
            pygame.draw.rect(win, self.YELLOW, bullet)
