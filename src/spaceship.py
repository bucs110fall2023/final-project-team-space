import pygame


class Spaceship(pygame.sprite.Sprite):
    VELOCITY = 5
    WIDTH, HEIGHT = 900, 500
    BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 2, HEIGHT)
    BORDER_COLOR = (255, 140, 0)

    def __init__(self, image_path, spaceship_width, spaceship_height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        scaled_img = pygame.transform.scale(self.image, (spaceship_width, spaceship_height))
        rotated_img = pygame.transform.rotate(scaled_img, 90)
        self.image = rotated_img
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def create_loading_image(self):
        loading_img = pygame.transform.rotozoom(self.image, 90, 2)
        return loading_img

    def render_start_menu_text(self, win):
        title_font = pygame.font.Font("font/Pixeltype.ttf", 36)
        instruction_font = pygame.font.Font("font/Pixeltype.ttf", 36)

        title_text = title_font.render("SPACE SHOOTER", False, (255, 255, 255))
        instruction_text = instruction_font.render("PRESS SPACE BAR TO START", False, (255, 255, 255))

        win.blit(title_text, (350, 100))
        win.blit(instruction_text, (300, 400))
