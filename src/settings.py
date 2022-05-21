import pygame

# Variable for the layout of the game
WIDTH = 1000
HEIGHT = 700
FPS = 60

ISLAND_WIDTH = 330
ISLAND_HEIGHT = 230

ATTACK_POINT_BOX_WIDTH = 100
ATTACK_POINT_BOX_HEIGHT = 50

DEFENSE_POINT_BOX_WIDTH = 100
DEFENSE_POINT_BOX_HEIGHT = 50

TEXT_FONT = "Avenir"
HEALTH_TEXT_SIZE = 35
ATTACK_TEXT_SIZE = 30
DEFENSE_TEXT_SIZE = 30
QUESTION_TEXT_SIZE = 20

# Initial variables at the start of the game
## Initial choice type of game
CHOICE_GAME = 0
random_activated = 0

winner_text = ""

## Initial points :
HEALTH_RED = 100
HEALTH_BLUE = 100
ATTACK_POINT_RED = 0
ATTACK_POINT_BLUE = 0
DEFENSE_POINT_RED = 0
DEFENSE_POINT_BLUE = 0
DEFENSE_RED_ACTIVATED = 0
DEFENSE_BLUE_ACTIVATED = 0

## Initial player turn :
PLAYER_TURN_RED = 1
PLAYER_TURN_BLUE = 0

## Player's turn layout variables
color_main_txt = ("red", "blue", "black")

Main_text = ("It's Player Red turn", "It's Player Blue turn")

index_blue = 1
index_red = 0


# Background image
b_img = pygame.image.load("resources/textures/Background/1.png")
b_img = pygame.transform.scale(b_img, (WIDTH, HEIGHT))

# Island image
isl_img0 = pygame.image.load("resources/textures/Island/ile0.001.png")
isl0 = pygame.transform.scale(isl_img0, (ISLAND_WIDTH, ISLAND_HEIGHT))
isl_img2 = pygame.image.load("resources/textures/Island/ile2.001.png")
isl2 = pygame.transform.scale(isl_img2, (ISLAND_WIDTH, ISLAND_HEIGHT))
isl_img4 = pygame.image.load("resources/textures/Island/ile4.001.png")
isl4 = pygame.transform.scale(isl_img4, (ISLAND_WIDTH, ISLAND_HEIGHT))
isl_img6 = pygame.image.load("resources/textures/Island/ile6.001.png")
isl6 = pygame.transform.scale(isl_img6, (ISLAND_WIDTH, ISLAND_HEIGHT))
isl_img8 = pygame.image.load("resources/textures/Island/ile8.001.png")
isl8 = pygame.transform.scale(isl_img8, (ISLAND_WIDTH, ISLAND_HEIGHT))
isl_img10 = pygame.image.load("resources/textures/Island/ile10.001.png")
isl10 = pygame.transform.scale(isl_img10, (ISLAND_WIDTH, ISLAND_HEIGHT))

isl_lvl = (isl0, isl2, isl4, isl6, isl8, isl10)