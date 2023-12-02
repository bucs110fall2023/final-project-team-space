import pygame
import sys

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
        # Create font objects
        title_font = pygame.font.Font('font/Pixeltype.ttf', 36)
        instruction_font = pygame.font.Font("font/Pixeltype.ttf", 36)

        # Text surfaces
        title_text = title_font.render("SPACE SHOOTER", True, (255, 255, 255))
        instruction_text = instruction_font.render("PRESS SPACEBAR TO START", True, (255, 255, 255))

        # Blit the text surfaces onto the screen
        win.blit(title_text, (350, 100))
        win.blit(instruction_text, (300, 400))

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

def main():
    pygame.init()
    clock = pygame.time.Clock()

    width, height = 900, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Space Shooter")

    # Load your background image
    background_img = pygame.image.load("assets/back.png")
    background_img = pygame.transform.scale(background_img, (width, height))

    # Create instances of the spaceship classes
    red_spaceship = RedSpaceship(100, 250)
    yellow_spaceship = YellowSpaceship(800, 250)

    # Create a sprite group and add the spaceships to it
    spaceship_group = pygame.sprite.Group()
    spaceship_group.add(red_spaceship, yellow_spaceship)

    # Define initial positions for the two background instances
    bg_x1, bg_x2 = 0, width

    # Game state variable
    game_running = False

    # Load scaled and rotated spaceship images for the loading screen
    red_spaceship_loading = red_spaceship.create_loading_image()
    yellow_spaceship_loading = yellow_spaceship.create_loading_image()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Check for space bar press to start the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_running = True

        if game_running:
            # Move the backgrounds
            bg_x1 -= 1
            bg_x2 -= 1

            # If the first background goes off-screen, reset its position
            if bg_x1 <= -width:
                bg_x1 = width

            # If the second background goes off-screen, reset its position
            if bg_x2 <= -width:
                bg_x2 = width

            # Draw the backgrounds
            win.blit(background_img, (bg_x1, 0))
            win.blit(background_img, (bg_x2, 0))

            # Draw the border
            pygame.draw.rect(win, Spaceship.BORDER_COLOR, Spaceship.BORDER)

            # Handle spaceship movements
            red_spaceship.handle_movement()
            yellow_spaceship.handle_movement()

            # Draw the spaceship group
            spaceship_group.draw(win)

        else:
            # Game loading menu, must click SPACE to continue
            win.fill((94, 129, 162))
            # Call the render_start_menu_text method for both spaceships
            red_spaceship.render_start_menu_text(win)
            yellow_spaceship.render_start_menu_text(win)
            # Blit the scaled and rotated spaceship images on the loading screen
            win.blit(red_spaceship_loading, (250, 250))
            win.blit(yellow_spaceship_loading, (550, 175))


        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()