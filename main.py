import pygame, sys
from src.methods import *
from pygame import mixer
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ISLAND WAR")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()


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

        self.defense_red_activated = DEFENSE_RED_ACTIVATED
        self.defense_blue_activated = DEFENSE_BLUE_ACTIVATED

        self.player_turn_red = PLAYER_TURN_RED
        self.player_turn_blue = PLAYER_TURN_BLUE

        self.index_red = index_red
        self.index_blue = index_blue





    def run(self):
        i = 1
        # Track:
        pygame.mixer.init()
        pygame.mixer.music.load("resources/Adieu Aru - Euphorie.mp3")
        pygame.mixer.music.play(-1)

        while True:
            # Background loop
            self.screen.fill((0, 0, 0))
            self.screen.blit(b_img, (i, 0))
            self.screen.blit(b_img, (WIDTH + i, 0))
            if i == - WIDTH:
                self.screen.blit(b_img, (WIDTH + i, 0))
                i = 0

            i -= 1
            # drawing islands
            self.screen.blit(isl_lvl[island_level(self.attack_point_blue)], (60, 220))
            self.screen.blit(pygame.transform.flip(isl_lvl[island_level((self.attack_point_red))],
                                                   True, False), (600, 220))

            # write attack point on the screen
            draw_attack_point(self.screen, self.attack_point_red, self.attack_point_blue)

            # write attack point on the screen
            draw_defense_point(self.screen, self.defense_point_red, self.defense_point_blue)

            # call 'draw_health_point' function
            draw_health_point(self.screen, self.health_red, self.health_blue)

            # write player's turn on the screen
            draw_player_turn(self.screen, self.player_turn_red, self.player_turn_blue)

            machine_choice = ai(self.player_turn_red)
            red_points(machine_choice, self)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    blue_points(event, self)


                # Background loop:

                self.clock.tick(FPS)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
