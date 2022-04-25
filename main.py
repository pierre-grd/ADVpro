import pygame, sys
from settings import *
from Methods import *
import os


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Advanced Programming Project - 2022")

        self.island_red = pygame.Rect(500, 200, ISLAND_WIDTH, ISLAND_HEIGHT)
        self.island_blue = pygame.Rect(100, 100, ISLAND_WIDTH, ISLAND_HEIGHT)

        self.attack_point_box_red = pygame.Rect(500, 150, ATTACK_POINT_BOX_WIDTH, ATTACK_POINT_BOX_HEIGHT)
        self.attack_point_box_blue = pygame.Rect(100, 50, ATTACK_POINT_BOX_WIDTH, ATTACK_POINT_BOX_HEIGHT)

        self.health_red = HEALTH_RED
        self.health_blue = HEALTH_BLUE

        self.attack_point_red = ATTACK_POINT_RED
        self.attack_point_blue = ATTACK_POINT_BLUE

        self.defense_point_red = DEFENSE_POINT_RED
        self.defense_point_blue = DEFENSE_POINT_BLUE

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.screen.fill("black")
                # draw rectangle for the islands
                pygame.draw.rect(self.screen, "red", self.island_red)
                pygame.draw.rect(self.screen, "blue", self.island_blue)

                # write attack point on the screen
                draw_attack_point(self.screen, self.attack_point_red, self.attack_point_blue)

                # write attack point on the screen
                draw_defense_point(self.screen, self.defense_point_red, self.defense_point_blue)

                # call 'draw_health_point' function
                draw_health_point(self.screen, HEALTH_RED, HEALTH_BLUE)

                # observe events and acts accordingly(still in crashtest)
                points(self.defense_point_red, self.defense_point_blue, self.attack_point_red, self.attack_point_blue,
                       HEALTH_RED, HEALTH_BLUE)

                self.clock.tick(FPS)

                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

