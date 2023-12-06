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
        title_font = pygame.font.Font(None, 36)
        instruction_font = pygame.font.Font(None, 36)

        title_text = title_font.render("SPACE SHOOTER", False, (255, 255, 255))
        instruction_text = instruction_font.render("PRESS SPACE BAR TO START", False, (255, 255, 255))

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


BULLET_VELOCITY = 7
red_bullets = []
yellow_bullets = []
MAX_BULLETS = 3

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in red_bullets:
        bullet.x += BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > Spaceship.WIDTH:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


def draw_window(red_bullets, yellow_bullets, win):
    for bullet in red_bullets:
        pygame.draw.rect(win, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(win, YELLOW, bullet)





def main():
    pygame.init()
    clock = pygame.time.Clock()

    red_health = 10
    yellow_health = 10


    width, height = 900, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Space Shooter")

    # Reset bullet lists at the beginning of each game
    red_bullets = []
    yellow_bullets = []

    background_img = pygame.image.load("assets/back.png")
    background_img = pygame.transform.scale(background_img, (width, height))

    red_spaceship = RedSpaceship(100, 250)
    yellow_spaceship = YellowSpaceship(800, 250)

    spaceship_group = pygame.sprite.Group()
    spaceship_group.add(red_spaceship, yellow_spaceship)

    bg_x1, bg_x2 = 0, width

    game_running = False

    red_spaceship_loading = red_spaceship.create_loading_image()
    yellow_spaceship_loading = yellow_spaceship.create_loading_image()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                elif event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red_spaceship.rect.x + red_spaceship.rect.width,
                        red_spaceship.rect.y + red_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    red_bullets.append(bullet)
                elif event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow_spaceship.rect.x,
                        yellow_spaceship.rect.y + yellow_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    yellow_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        if game_running:
            bg_x1 -= 1
            bg_x2 -= 1

            if bg_x1 <= -width:
                bg_x1 = width

            if bg_x2 <= -width:
                bg_x2 = width

            win.blit(background_img, (bg_x1, 0))
            win.blit(background_img, (bg_x2, 0))

            pygame.draw.rect(win, Spaceship.BORDER_COLOR, Spaceship.BORDER)

            red_spaceship.handle_movement()
            yellow_spaceship.handle_movement()

            spaceship_group.draw(win)

            handle_bullets(yellow_bullets, red_bullets, yellow_spaceship.rect, red_spaceship.rect)
            draw_window(red_bullets, yellow_bullets, win)

            # Add these lines at the beginning of your code
            health_font = pygame.font.Font(None, 36)

            # Draw health scores
            red_health_text = health_font.render(f"Red Health: {red_health}", True, (255, 0, 0))
            yellow_health_text = health_font.render(f"Yellow Health: {yellow_health}", True, (255, 255, 0))
            win.blit(red_health_text, (10, 10))  # Top-left corner
            win.blit(yellow_health_text, (width - yellow_health_text.get_width() - 10, 10))  # Top-right corner

            # Check for winner
            if yellow_health <= 0 or red_health <= 0:
                winner_text = "RED WINS!" if yellow_health <= 0 else "YELLOW WINS!"
                winner_font = pygame.font.Font(None, 72)
                winner_text_rendered = winner_font.render(winner_text, True, (255, 255, 255))
                win.blit(winner_text_rendered, (width // 2 - winner_text_rendered.get_width() // 2,
                                                height // 2 - winner_text_rendered.get_height() // 2))
                pygame.display.update()
                pygame.time.delay(3000)  # Display winner for 3 seconds
                run = False
                main()

        else:
            win.fill((94, 129, 162))
            red_spaceship.render_start_menu_text(win)
            yellow_spaceship.render_start_menu_text(win)
            win.blit(red_spaceship_loading, (250, 250))
            win.blit(yellow_spaceship_loading, (550, 175))

        pygame.display.update()
        clock.tick(60)

    # main()


if __name__ == "__main__":
    main()
