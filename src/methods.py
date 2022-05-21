import pygame, sys
from src.settings import *
import random
import time

def draw_background(screen, b_img, i):
    """
      Display the background of the game.
      For loop to make the background move : wave effect.
    """
    screen.fill((0, 0, 0))
    screen.blit(b_img, (i, 0))
    screen.blit(b_img, (WIDTH + i, 0))
    if i == - WIDTH:
        screen.blit(b_img, (WIDTH + i, 0))
        i = 0
    i -= 1


def draw_health_point(screen, health_red, health_blue):
    """
    Write health points of the players on the screen.
    """
    health_font = pygame.font.SysFont(TEXT_FONT, HEALTH_TEXT_SIZE)
    health_text_red = health_font.render("Health: " + str(health_red), True, "red")
    health_text_blue = health_font.render("Health: " + str(health_blue), True, "blue")
    screen.blit(health_text_red, (650, 430))
    screen.blit(health_text_blue, (100, 430))


def draw_attack_point(screen, attack_point_red, attack_point_blue):
    """
    Write attack points of the players on the screen.
    """
    attack_point_font = pygame.font.SysFont(TEXT_FONT, ATTACK_TEXT_SIZE)
    attack_text_red = attack_point_font.render(
        "Attack point: " + str(attack_point_red), True, "white")
    attack_text_blue = attack_point_font.render(
        "Attack point: " + str(attack_point_blue), True, "white")
    screen.blit(attack_text_red, (650, 250))
    screen.blit(attack_text_blue, (100, 250))


def draw_defense_point(screen, defense_point_red, defense_point_blue):
    """
    Write defense points of the players on the screen.
    """
    defense_point_font = pygame.font.SysFont(TEXT_FONT, DEFENSE_TEXT_SIZE)
    defense_text_red = defense_point_font.render(
        "Defense point: " + str(defense_point_red), True, "white")
    defense_text_blue = defense_point_font.render(
        "Defense point: " + str(defense_point_blue), True, "white")
    screen.blit(defense_text_red, (650, 270))
    screen.blit(defense_text_blue, (100, 270))


def draw_player_turn(screen, player_turn_red, player_turn_blue):
    """
    Write a sentence indicating which player's turn it is.
    """
    health_font = pygame.font.SysFont(TEXT_FONT, 50)
    if player_turn_red == 1:
        player_turn_text = health_font.render(Main_text[index_red], True, color_main_txt[0])
    elif player_turn_blue == 1:
        player_turn_text = health_font.render(Main_text[index_blue], True, color_main_txt[1])
    screen.blit(player_turn_text, (HEIGHT / 2, 630))

def draw_opening_question(screen, choice_game):
    """
    Write a sentence starting sentence for the player to choose if the game is.
    """
    opening_question_font = pygame.font.SysFont(TEXT_FONT, QUESTION_TEXT_SIZE)
    if choice_game == 0:
        question_text_red = opening_question_font.render(
            "Choose whether it is player against computer(press 1) or player against player (press 2) ",
        True, "white")
    screen.blit(question_text_red, (120, 75))

def draw_winner(screen, health_red, health_blue):
    """
    Write the winner player on the screen.
    """
    winner_text_font = pygame.font.SysFont(TEXT_FONT, 50)
    if health_red <= 0:
        winner_text = winner_text_font.render(
            "The player Blue won !!",True, "blue")
    elif health_blue <= 0:
        winner_text = winner_text_font.render(
            "The player Red won !!", True, "red")

    screen.blit(winner_text, (250, 275))
    pygame.display.update()
    pygame.time.delay(5000)

def choice_type_game(event, self):
    """
    Function for the player to choose the type of the game.
    - For one player (press 1) : the player will play against the computer
    - For two players (press 2) : both players play against one another
    """
    if event.key == pygame.K_1 and self.choice_game == 0:
        self.random_activated = 1
        self.choice_game = 1
    elif event.key == pygame.K_2 and self.choice_game == 0:
        self.random_activated = 0
        self.choice_game = 2

def blue_points(event, self):
    """
    Function that computes the points for the player blue depending on the action he does.
    It subtracts or adds points depending on they key pressed and then shift the turn to player red.
    - (Press 's') : the player increases its defense points
    - (Press 'w') : the player increases its attack points
    - (Press 'd') : the player decreases its opponent's points
    - (Press 'a') : the player activate its defense for the next attack he gets
    """

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

    elif event.key == pygame.K_d and self.player_turn_blue == 1:
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

    elif event.key == pygame.K_a and self.player_turn_blue == 1:
        # player blue : activate defense against opponent's next attack
        self.defense_blue_activated += 1
        self.player_turn_blue -= 1
        self.player_turn_red += 1

def red_points(event, self):
    """
    Function that computes the points for the player red depending on the action he does.
    It subtracts or adds points depending on they key pressed and then shift the turn to player blue.
    - (Press 'DOWN') : the player increases its defense points
    - (Press 'UP') : the player increases its attack points
    - (Press 'LEFT') : the player decreases its opponent's points
    - (Press 'RIGHT') : the player activate its defense for the next attack he gets
    """

    if event.key == pygame.K_DOWN and self.player_turn_red == 1 and self.defense_point_red < 10:
        # player red : invest in defense
        def_minus = random.randint(3, 4)
        self.defense_point_red += def_minus
        self.player_turn_red -= 1
        self.player_turn_blue += 1
        if self.defense_point_red > 10:
            self.defense_point_red = 10

    elif event.key == pygame.K_UP and self.player_turn_red == 1 and self.attack_point_red != 10:
        # player red : invest in attack
        self.attack_point_red += 2
        self.player_turn_red -= 1
        self.player_turn_blue += 1

    elif event.key == pygame.K_LEFT and self.player_turn_red == 1:
        # player red : attack its opponent
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
        # player red : activate defense against opponent's next attack
        self.defense_red_activated += 1
        self.player_turn_red -= 1
        self.player_turn_blue += 1

def red_points_random(random_event, self):
    """
    Function that computes the points for the computer player red depending on the random action generated.
    It subtracts or adds points depending random key generated by another function,
    and then shift the turn to player blue.
    - (Randomnized 'DOWN') : the computer player increases its defense points
    - (Randomnized 'UP') : the computer player increases its attack points
    - (Randomnized 'LEFT') : the computer player decreases its opponent's points
    - (Randomnized 'RIGHT') : the computer player activate its defense for the next attack he gets
    """

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
    """
    Function that select at random a key between (RIGHT, LEFT, UP and DOWN).
    This function is activated when the player decides to play against a computer
    and that it is the computer's turn to play.
    """

    key_list = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
    if player_turn_red == 1 and random_activated == 1:
        random_key = random.choice(key_list)
        return random_key

def island_level(level):
    """
    Matches the level of the player (based on its amount of defense points)
    to the islands image corresponding (the number of cannons changes).
    """
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
