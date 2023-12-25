import pygame


class Spaceship(pygame.sprite.Sprite):
    """
    A class representing a spaceship in a game using Pygame.

    Attributes:
        VELOCITY (int): The constant velocity of the spaceship.
        WIDTH (int): The width of the game window.
        HEIGHT (int): The height of the game window.
        BORDER (pygame.Rect): A rectangle representing the border of the game window.
        BORDER_COLOR (tuple): The RGB color tuple for the border color.

    Methods:
        __init__(self, image_path, spaceship_width, spaceship_height, pos_x, pos_y):
            Initializes a Spaceship object.

        create_loading_image(self):
            Creates and returns a loading image by rotating and zooming the spaceship image.

        render_start_menu_text(self, win):
            Renders the start menu text on the game window.

    """  
    VELOCITY = 5
    WIDTH, HEIGHT = 900, 500
    BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 2, HEIGHT)
    BORDER_COLOR = (255, 140, 0)

    def __init__(self, image_path, spaceship_width, spaceship_height, pos_x, pos_y):
        """
        Initializes a Spaceship object.

        Args:
            image_path (str): The path to the image file for the spaceship.
            spaceship_width (int): The width of the spaceship.
            spaceship_height (int): The height of the spaceship.
            pos_x (int): The initial x-coordinate of the spaceship.
            pos_y (int): The initial y-coordinate of the spaceship.
        """    
        super().__init__()
        self.image = pygame.image.load(image_path)
        scaled_img = pygame.transform.scale(self.image, (spaceship_width, spaceship_height))
        rotated_img = pygame.transform.rotate(scaled_img, 90)
        self.image = rotated_img
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def create_loading_image(self):
        """
        Creates and returns a loading image by rotating and zooming the spaceship image.

        Returns:
            pygame.Surface: The loading image surface.
        """
        loading_img = pygame.transform.rotozoom(self.image, 90, 2)
        return loading_img

    def render_start_menu_text(self, win):
        """
        Renders the start menu text on the game window.

        Args:
            win (pygame.Surface): The game window surface.
        """
        title_font = pygame.font.Font("font/Pixeltype.ttf", 36)
        instruction_font = pygame.font.Font("font/Pixeltype.ttf", 36)

        title_text = title_font.render("SPACE SHOOTER", False, (255, 255, 255))
        instruction_text = instruction_font.render("PRESS SPACE BAR TO START", False, (255, 255, 255))

        win.blit(title_text, (350, 100))
        win.blit(instruction_text, (300, 400))
