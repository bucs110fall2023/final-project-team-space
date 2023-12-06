import pygame
from src.controller import GameController
from src.model import GameModel
from src.view import GameView

def main():
    pygame.init()

    # Create instances of your model and view
    model = GameModel()
    view = GameView()

    # Create an instance of your controller
    controller = GameController(model, view)

    # Call the main loop of your controller
    controller.main_loop()

if __name__ == '__main__':
    main()
