import pygame, sys
from settings import *


def draw_health_point(screen, health_red, health_blue):
    # write health point on the screen
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    health_text_red = health_font.render("Health: " + str(health_red), 1, "green")
    health_text_blue = health_font.render("Health: " + str(health_blue), 1, "green")
    screen.blit(health_text_red, (500, 400))
    screen.blit(health_text_blue, (100, 300))


def draw_attack_point(screen, attack_point_red, attack_point_blue):
    # write attack point on the screen
    attack_point_font = pygame.font.SysFont(TEXT_FONT, ATTACK_TEXT_SIZE)
    attack_text_red = attack_point_font.render(
        "Attack point: " + str(attack_point_red), 1, "white")
    attack_text_blue = attack_point_font.render(
        "Attack point: " + str(attack_point_blue), 1, "white")
    screen.blit(attack_text_red, (500, 175))
    screen.blit(attack_text_blue, (100, 75))


def draw_defense_point(screen, defense_point_red, defense_point_blue):
    # write attack point on the screen
    defense_point_font = pygame.font.SysFont(TEXT_FONT, DEFENSE_TEXT_SIZE)
    defense_text_red = defense_point_font.render(
        "Defense point: " + str(defense_point_red), 1, "white")
    defense_text_blue = defense_point_font.render(
        "Defense point: " + str(defense_point_blue), 1, "white")
    screen.blit(defense_text_red, (500, 155))
    screen.blit(defense_text_blue, (100, 55))


def points(defense_point_red, defense_point_blue, attack_point_red, attack_point_blue,
           health_point_red, health_point_blue):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                defense_point_blue += 2
                # Pour tester si l'input est prit en compte
                print("s")
            elif event.key == pygame.K_DOWN:
                defense_point_red += 2
            elif event.key == pygame.K_UP:
                attack_point_red += 2
                print("kup")
            elif event.key == pygame.K_w:
                attack_point_blue += -1
            elif event.key == pygame.K_a:
                health_point_blue += -1
                print("a")
            elif event.key == pygame.K_LEFT:
                health_point_red += -attack_point_blue
