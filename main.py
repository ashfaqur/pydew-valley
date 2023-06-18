import sys

import pygame

from settings import *

GAME_TITLE = 'Py-Dew Valley'


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                self.do_quit(event)
            dt = self.clock.tick() / 1000
            pygame.display.update()

    def do_quit(self, event):
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
