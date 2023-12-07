import pygame
from src.red_spaceship import RedSpaceship
from src.yellow_spaceship import YellowSpaceship
from src.game_manager import GameManager
from src.spaceship import Spaceship


class SpaceShooterGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.red_health = 12
        self.yellow_health = 12
        self.game_manager = GameManager()

        self.width, self.height = 900, 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Shooter")

        self.background_img = pygame.image.load("assets/back.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.width, self.height))

        self.red_spaceship = RedSpaceship(100, 250)
        self.yellow_spaceship = YellowSpaceship(800, 250)

        self.spaceship_group = pygame.sprite.Group()
        self.spaceship_group.add(self.red_spaceship, self.yellow_spaceship)

        self.bg_x1, self.bg_x2 = 0, self.width
        self.game_running = False

        self.red_spaceship_loading = self.red_spaceship.create_loading_image()
        self.yellow_spaceship_loading = self.yellow_spaceship.create_loading_image()

        self.hit_sound = pygame.mixer.Sound("assets/Grenade+1.mp3")
        self.shoot_sound = pygame.mixer.Sound("assets/Gun+Silencer.mp3")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_running = True
                elif event.key == pygame.K_LCTRL and len(self.game_manager.red_bullets) < self.game_manager.MAX_BULLETS:
                    bullet = pygame.Rect(
                        self.red_spaceship.rect.x + self.red_spaceship.rect.width,
                        self.red_spaceship.rect.y + self.red_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    self.game_manager.red_bullets.append(bullet)
                    self.shoot_sound.play()
                elif event.key == pygame.K_RCTRL and len(self.game_manager.yellow_bullets) < self.game_manager.MAX_BULLETS:
                    bullet = pygame.Rect(
                        self.yellow_spaceship.rect.x,
                        self.yellow_spaceship.rect.y + self.yellow_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    self.game_manager.yellow_bullets.append(bullet)
                    self.shoot_sound.play()

            if event.type == self.game_manager.RED_HIT:
                self.red_health -= 1
                self.hit_sound.play()

            if event.type == self.game_manager.YELLOW_HIT:
                self.yellow_health -= 1
                self.hit_sound.play()


    def reset_game(self):
        self.red_health = 12
        self.yellow_health = 12
        self.red_spaceship.rect.topleft = (100, 250)
        self.yellow_spaceship.rect.topleft = (800, 250)
        self.game_manager.red_bullets.clear()
        self.game_manager.yellow_bullets.clear()
        self.bg_x1, self.bg_x2 = 0, self.width
        self.game_running = False
   
   
    def main_loop(self):
        while True:
            self.handle_events()

            if self.game_running:
                self.game_manager.handle_bullets(self.yellow_spaceship.rect, self.red_spaceship.rect)

                self.bg_x1 -= 1
                self.bg_x2 -= 1

                if self.bg_x1 <= -self.width:
                    self.bg_x1 = self.width

                if self.bg_x2 <= -self.width:
                    self.bg_x2 = self.width

                self.win.blit(self.background_img, (self.bg_x1, 0))
                self.win.blit(self.background_img, (self.bg_x2, 0))

                pygame.draw.rect(self.win, Spaceship.BORDER_COLOR, Spaceship.BORDER)

                self.red_spaceship.handle_movement()
                self.yellow_spaceship.handle_movement()

                self.spaceship_group.draw(self.win)
                self.game_manager.draw_window(self.win)

                health_font = pygame.font.Font("font/Pixeltype.ttf", 36)
                red_health_text = health_font.render(f"Red Health: {self.red_health}", True, (255, 0, 0))
                yellow_health_text = health_font.render(f"Yellow Health: {self.yellow_health}", True, (255, 255, 0))
                self.win.blit(red_health_text, (120, 10))
                self.win.blit(yellow_health_text, (self.width - yellow_health_text.get_width() - 120, 10))

                if self.yellow_health <= 0 or self.red_health <= 0:
                    winner_text = "RED WINS!" if self.yellow_health <= 0 else "YELLOW WINS!"
                    winner_font = pygame.font.Font("font/Pixeltype.ttf", 72)
                    winner_text_rendered = winner_font.render(winner_text, True, (255, 255, 255))
                    self.win.blit(winner_text_rendered, (self.width // 2 - winner_text_rendered.get_width() // 2,
                                                         self.height // 2 - winner_text_rendered.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    self.reset_game()

            else:
                self.win.fill((94, 129, 162))
                self.red_spaceship.render_start_menu_text(self.win)
                self.yellow_spaceship.render_start_menu_text(self.win)
                self.win.blit(self.red_spaceship_loading, (250, 250))
                self.win.blit(self.yellow_spaceship_loading, (550, 175))

            pygame.display.update()
            self.clock.tick(60)