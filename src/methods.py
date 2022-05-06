import pygame, sys
from src.settings import *
import random
import time

def draw_background(screen, b_img, i):
    screen.fill((0, 0, 0))
    screen.blit(b_img, (i, 0))
    screen.blit(b_img, (WIDTH + i, 0))
    if i == - WIDTH:
        screen.blit(b_img, (WIDTH + i, 0))
        i = 0
    i -= 1


def draw_health_point(screen, health_red, health_blue):
    # write health point on the screen
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    health_text_red = health_font.render("Health: " + str(health_red), True, "red")
    health_text_blue = health_font.render("Health: " + str(health_blue), True, "blue")
    screen.blit(health_text_red, (650, 430))
    screen.blit(health_text_blue, (100, 430))


def draw_attack_point(screen, attack_point_red, attack_point_blue):
    # write attack point on the screen
    attack_point_font = pygame.font.SysFont(TEXT_FONT, ATTACK_TEXT_SIZE)
    attack_text_red = attack_point_font.render(
        "Attack point: " + str(attack_point_red), True, "white")
    attack_text_blue = attack_point_font.render(
        "Attack point: " + str(attack_point_blue), True, "white")
    screen.blit(attack_text_red, (650, 250))
    screen.blit(attack_text_blue, (100, 250))


def draw_defense_point(screen, defense_point_red, defense_point_blue):
    # write attack point on the screen
    defense_point_font = pygame.font.SysFont(TEXT_FONT, DEFENSE_TEXT_SIZE)
    defense_text_red = defense_point_font.render(
        "Defense point: " + str(defense_point_red), True, "white")
    defense_text_blue = defense_point_font.render(
        "Defense point: " + str(defense_point_blue), True, "white")
    screen.blit(defense_text_red, (650, 270))
    screen.blit(defense_text_blue, (100, 270))


def draw_player_turn(screen, player_turn_red, player_turn_blue):
    # write whose player's turn is it
    health_font = pygame.font.SysFont(TEXT_FONT, 50)
    if player_turn_red == 1:
        player_turn_text = health_font.render(Main_text[index_red], True, color_main_txt[0])
    elif player_turn_blue == 1:
        player_turn_text = health_font.render(Main_text[index_blue], True, color_main_txt[1])
    screen.blit(player_turn_text, (HEIGHT / 2, 630))

def draw_opening_question(screen, choice_game):
    opening_question_font = pygame.font.SysFont(TEXT_FONT, QUESTION_TEXT_SIZE)
    if choice_game == 0:
        question_text_red = opening_question_font.render(
            "Choose whether it is player against computer(press 1) or player against player (press 2) ",
        True, "white")
    screen.blit(question_text_red, (150, 75))

def draw_winner(screen, health_red, health_blue):
    winner_text_font = pygame.font.SysFont(TEXT_FONT, 50)
    if health_red <= 0:
        winner_text = winner_text_font.render(
            "The player Red won !!",True, "red")
    elif health_blue <= 0:
        winner_text = winner_text_font.render(
            "The player Blue won !!", True, "blue")

    screen.blit(winner_text, (150, 275))
    pygame.time.delay(5000)

def choice_type_game(event, self):
    if event.key == pygame.K_1 and self.choice_game == 0:
        self.random_activated = 1
        self.choice_game = 1
    elif event.key == pygame.K_2 and self.choice_game == 0:
        self.random_activated = 0
        self.choice_game = 2

def blue_points(event, self):
    # subtract or add points depending on the key pressed
    if event.key == pygame.K_s and self.player_turn_blue == 1 and self.defense_point_blue < 10:
        # player blue : invest in defense
        def_minus = random.randint(3,4)
        self.defense_point_blue += def_minus
        self.player_turn_blue -= 1
        self.player_turn_red += 1
        if self.defense_point_blue > 10:
            self.defense_point_blue = 10

    elif event.key == pygame.K_w and self.player_turn_blue == 1 and self.attack_point_blue != 10:
        # player blue : invest in attack
        self.attack_point_blue += 2
        self.player_turn_blue -= 1
        self.player_turn_red += 1

    elif event.key == pygame.K_a and self.player_turn_blue == 1:
        # player blue : attack its opponent
        if self.defense_red_activated == 1:
            self.health_red += -self.attack_point_blue + self.defense_point_red
            self.defense_red_activated -= 1
            self.player_turn_blue -= 1
            self.player_turn_red += 1
        else:
            self.health_red += -self.attack_point_blue
            self.player_turn_blue -= 1
            self.player_turn_red += 1

    elif event.key == pygame.K_d and self.player_turn_blue == 1:
        # player blue : activate defense against opponent's next attack
        self.defense_blue_activated += 1
        self.player_turn_blue -= 1
        self.player_turn_red += 1

def red_points(event, self):
    # subtract or add points depending on the key pressed
    if event.key == pygame.K_DOWN and self.player_turn_red == 1 and self.defense_point_red < 10:
        # player blue : invest in defense
        def_minus = random.randint(3, 4)
        self.defense_point_red += def_minus
        self.player_turn_red -= 1
        self.player_turn_blue += 1
        if self.defense_point_red > 10:
            self.defense_point_red = 10

    elif event.key == pygame.K_UP and self.player_turn_red == 1 and self.attack_point_red != 10:
        # player blue : invest in attack
        self.attack_point_red += 2
        self.player_turn_red -= 1
        self.player_turn_blue += 1

    elif event.key == pygame.K_LEFT and self.player_turn_red == 1:
        # player blue : attack its opponent
        if self.defense_blue_activated == 1:
            self.health_red += -self.attack_point_red + self.defense_point_blue
            self.defense_blue_activated -= 1
            self.player_turn_red -= 1
            self.player_turn_blue += 1
        else:
            self.health_blue += -self.attack_point_red
            self.player_turn_red -= 1
            self.player_turn_blue += 1

    elif event.key == pygame.K_RIGHT and self.player_turn_red == 1:
        # player blue : activate defense against opponent's next attack
        self.defense_red_activated += 1
        self.player_turn_red -= 1
        self.player_turn_blue += 1

def red_points_random(random_event, self):
    if random_event == pygame.K_DOWN and self.player_turn_red == 1 and self.defense_point_red != 10:
        # player red : invest in defense
        def_minus = random.randint(3, 4)
        self.defense_point_red += def_minus
        self.player_turn_red -= 1
        self.player_turn_blue += 1
        if self.defense_point_red > 10:
            self.defense_point_red = 10
    elif random_event == pygame.K_UP and self.player_turn_red == 1 and self.attack_point_red != 10:
        # player red : invest in attack
        self.attack_point_red += 2
        self.player_turn_red -= 1
        self.player_turn_blue += 1

    elif random_event == pygame.K_LEFT and self.player_turn_red == 1:
        # player red : attack its opponent
        if self.defense_blue_activated == 1:
            self.health_blue += -self.attack_point_red + self.defense_point_blue
            self.defense_blue_activated -= 1
            self.player_turn_red -= 1
            self.player_turn_blue += 1
        else:
            self.health_blue += -self.attack_point_red
            self.player_turn_red -= 1
            self.player_turn_blue += 1

    elif random_event == pygame.K_RIGHT and self.player_turn_red == 1:
        # player red : activate defense against opponent's next attack
        self.defense_red_activated += 1
        self.player_turn_red -= 1
        self.player_turn_blue += 1


def ai(player_turn_red, random_activated):
    key_list = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
    if player_turn_red == 1 and random_activated == 1:
        random_key = random.choice(key_list)
        return random_key

def island_level(level):
    match level:
        case 0:
            return int(0)
        case 2:
            return int(1)
        case 4:
            return int(2)
        case 6:
            return int(3)
        case 8:
            return int(4)
        case 10:
            return int(5)
