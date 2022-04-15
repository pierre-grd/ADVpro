import pygame, sys
from settings import *

def draw_health_point(screen, health_red, health_blue):
    # write health point on the screen
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    health_text_red = health_font.render("Health: " + str(health_red), 1, "green")
    health_text_blue = health_font.render("Health: " + str(health_blue), 1, "green")
    screen.blit(health_text_red, (500, 500))
    screen.blit(health_text_blue, (100, 400))


def draw_attack_point(screen, attack_point_red, attack_point_blue):
    # write attack point on the screen
    attack_point_font = pygame.font.SysFont(TEXT_FONT, ATTACK_TEXT_SIZE)
    attack_text_red = attack_point_font.render(
        "Attack point: " + str(attack_point_red), 1, "white")
    attack_text_blue = attack_point_font.render(
        "Attack point: " + str(attack_point_blue), 1, "white")
    screen.blit(attack_text_red, (500, 175))
    screen.blit(attack_text_blue, (100, 75))