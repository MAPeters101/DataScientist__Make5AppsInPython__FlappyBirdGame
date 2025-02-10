import random
import sys
import pygame
from pygame.locals import *

FPS = 32
screen_width = 289
screen_height = 511
window = pygame.display.set_mode((screen_width,screen_height))
play_area = screen_height * 0.8
game_image = {}
game_audio_sound = {}
player = 'images/bird.png'
background_image = 'images/background.png'
pipe_image = 'images/pipe.png'

def welcome_main_screen():
    p_x = int(screen_width/5)
    p_y = int(screen_height - game_image['player'].get_height()/2)
    msgx = int((screen_width-game_image['message'].get_width())/2)
    msgy = int(screen_height * 0.13)
    b_x = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                window.blit(game_image['background'],(0,0))
                window.blit(game_image['player'],(p_x,p_y))
                window.blit(game_image['message'],(msgx,msgy))
                window.blit(game_image['base'],(b_x,play_area))
                pygame.display.update()
                time_clock.tick(FPS)







if __name__=="__main__":
    pygame.init()
    time_clock = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird Game")
    game_image['numbers'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )

    #game_image['message'] = pygame.image.load('images/message.png').convert_alpha()
    game_image['base'] = pygame.image.load('images/base.png').convert_alpha()
    game_image['pipe'] = (pygame.transform.rotate(pygame.image.load(pipe_image).convert_alpha(),180),
                          pygame.image.load(pipe_image).convert_alpha())

    game_audio_sound['die'] = pygame.mixer.Sound('sounds/die.wav')
    game_audio_sound['hit'] = pygame.mixer.Sound('sounds/hit.wav')
    game_audio_sound['point'] = pygame.mixer.Sound('sounds/point.wav')
    game_audio_sound['swoosh'] = pygame.mixer.Sound('sounds/swoosh.wav')
    game_audio_sound['wing'] = pygame.mixer.Sound('sounds/wing.wav')

    game_image['background'] = pygame.image.load(background_image).convert()
    game_image['player'] = pygame.image.load(player).convert()

    while True:
        welcome_main_screen()
        main_gameplay()

