import pygame

# General setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Global Variables
bg_color = pygame.Color('#2F373F')
accent_color = (27,35,43)
basic_font = pygame.font.Font('8-BIT WONDER.TTF', 32)
plob_sound = pygame.mixer.Sound("./multimedia/pong.ogg")
score_sound = pygame.mixer.Sound("./multimedia/score.ogg")
mario_sound = pygame.mixer.Sound("./multimedia/mario.ogg")
luigi_sound = pygame.mixer.Sound("./multimedia/luigi.ogg")
middle_strip = pygame.Rect(screen_width/2 - 2,0,4,screen_height)