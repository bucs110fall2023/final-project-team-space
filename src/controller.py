import pygame
from draft_2 import Spaceship, RedSpaceship, YellowSpaceship

class Controller(Spaceship):
  def __init__(self,velocity,max_bullets, red, yellow,yellow_hit,red_hit,red_bullets,yellow_bullets,clock,red_health,yellow_health, width, height,win):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.red_health = 10
    self.yellow_health = 10
    self.width, self.height = 900, 500
    self.win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Space Shooter")
    self.velocity = 7
    self.red_bullets = []
    self.yellow_bullets = []
    self.max_bullets = 3
    self.red = (255, 0, 0)
    self.yellow = (255, 255, 0)
    self.yellow_hit = pygame.USEREVENT + 1
    self.red_hit = pygame.USEREVENT + 2
    
  def mainloop(self):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                elif event.key == pygame.K_LCTRL and len(self.red_bullets) < self.max_bullets:
                    bullet = pygame.Rect(
                        self.red_spaceship.rect.x + red_spaceship.rect.width,
                        self.red_spaceship.rect.y + red_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    self.red_bullets.append(bullet)
                elif event.key == pygame.K_RCTRL and len(self.yellow_bullets) < self.max_bullets:
                    bullet = pygame.Rect(
                        yellow_spaceship.rect.x,
                        yellow_spaceship.rect.y + yellow_spaceship.rect.height / 2 - 2,
                        10, 5
                    )
                    self.yellow_bullets.append(bullet)

            if event.type == self.red_hit:
                self.red_health -= 1

            if event.type == self.yellow_hit:
                self.yellow_health -= 1

        if game_running:
            bg_x1 -= 1
            bg_x2 -= 1

            if bg_x1 <= -self.width:
                bg_x1 = self.width

            if bg_x2 <= -self.width:
                bg_x2 = self.width

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
        self.clock.tick(60)

    # main()
if __name__ == "__main__":
    main()
    
  
