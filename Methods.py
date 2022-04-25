import pygame, sys
from settings import *


def draw_health_point(screen, health_red, health_blue):
    # write health point on the screen
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    health_text_red = health_font.render("Health: " + str(health_red), True, "green")
    health_text_blue = health_font.render("Health: " + str(health_blue), True, "green")
    screen.blit(health_text_red, (500, 400))
    screen.blit(health_text_blue, (100, 300))


def draw_attack_point(screen, attack_point_red, attack_point_blue):
    # write attack point on the screen
    attack_point_font = pygame.font.SysFont(TEXT_FONT, ATTACK_TEXT_SIZE)
    attack_text_red = attack_point_font.render(
        "Attack point: " + str(attack_point_red), True, "white")
    attack_text_blue = attack_point_font.render(
        "Attack point: " + str(attack_point_blue), True, "white")
    screen.blit(attack_text_red, (500, 175))
    screen.blit(attack_text_blue, (100, 75))


def draw_defense_point(screen, defense_point_red, defense_point_blue):
    # write attack point on the screen
    defense_point_font = pygame.font.SysFont(TEXT_FONT, DEFENSE_TEXT_SIZE)
    defense_text_red = defense_point_font.render(
        "Defense point: " + str(defense_point_red), True, "white")
    defense_text_blue = defense_point_font.render(
        "Defense point: " + str(defense_point_blue), True, "white")
    screen.blit(defense_text_red, (500, 155))
    screen.blit(defense_text_blue, (100, 55))

def draw_player_turn(screen, player_turn_red, player_turn_blue):
    # write whose player's turn is it
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    if player_turn_red == 1:
        player_turn_text = health_font.render("Player RED, your turn to play ", True, "yellow")
    elif player_turn_blue == 1:
        player_turn_text = health_font.render("Player BLUE, your turn to play ", True, "yellow")
    screen.blit(player_turn_text, (275, 500))

# ajouter une sortie de boucle a chaque input réalisé
def points(event, self):
    # subtract or add points depending on the key pressed
    if event.key == pygame.K_s and self.player_turn_blue == 1:
        self.defense_point_blue += 2
        self.player_turn_blue -= 1
        self.player_turn_red += 1
        # Pour tester si l'input est prit en compte
        print("s")
        print(self.defense_point_blue)
        print(self.player_turn_blue)
        print(self.player_turn_red)
    elif event.key == pygame.K_DOWN and self.player_turn_red == 1:
        self.defense_point_red += 2
        self.player_turn_red -= 1
        self.player_turn_blue += 1
    elif event.key == pygame.K_UP and self.player_turn_red == 1:
        self.attack_point_red += 2
        self.player_turn_red -= 1
        self.player_turn_blue += 1
        print("kup")
    elif event.key == pygame.K_w and self.player_turn_blue == 1:
        self.attack_point_blue += -1
        self.player_turn_blue -= 1
        self.player_turn_red += 1
    elif event.key == pygame.K_a and self.player_turn_blue == 1:
        self.health_blue += -1
        self.player_turn_blue -= 1
        self.player_turn_red += 1
        print("a")
    elif event.key == pygame.K_LEFT and self.player_turn_red == 1:
        self.health_red += -self.attack_point_blue
        self.player_turn_red -= 1
        self.player_turn_blue += 1
