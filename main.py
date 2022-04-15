import pygame, sys
from settings import *
import os


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption("Advanced Programming Project - 2022")

        self.island_red = pygame.Rect(500, 200, ISLAND_WIDTH, ISLAND_HEIGHT)
        self.island_blue = pygame.Rect(100, 100, ISLAND_WIDTH, ISLAND_HEIGHT)

        self.attack_point_box_red = pygame.Rect(500, 150, ATTACK_POINT_BOX_WIDTH, ATTACK_POINT_BOX_HEIGHT)
        self.attack_point_box_blue = pygame.Rect(100, 50, ATTACK_POINT_BOX_WIDTH, ATTACK_POINT_BOX_HEIGHT)

        self.health_point_box_red = pygame.Rect(500, 450, HEALTH_POINT_BOX_WIDTH, HEALTH_POINT_BOX_HEIGHT)
        self.health_point_box_blue = pygame.Rect(100, 350, HEALTH_POINT_BOX_WIDTH, HEALTH_POINT_BOX_HEIGHT)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            # draw rectangle for the islands
            pygame.draw.rect(self.screen, "white", self.island_red)
            pygame.draw.rect(self.screen, "white", self.island_blue)
            # draw rectangle for the points of attack
            pygame.draw.rect(self.screen, "red", self.attack_point_box_red)
            pygame.draw.rect(self.screen, "red", self.attack_point_box_blue)
            # draw rectangle for the points of health
            pygame.draw.rect(self.screen, "red", self.health_point_box_red)
            pygame.draw.rect(self.screen, "red", self.health_point_box_blue)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
