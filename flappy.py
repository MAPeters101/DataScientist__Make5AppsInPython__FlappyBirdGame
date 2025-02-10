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
    ##msgx = int((screen_width-game_image['message'].get_width())/2)
    ##msgy = int(screen_height * 0.13)
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
                ##window.blit(game_image['message'],(msgx,msgy))
                window.blit(game_image['base'],(b_x,play_area))
                pygame.display.update()
                time_clock.tick(FPS)


def get_Random_Pipes():
    pass


def main_gameplay():
    score = 0
    p_x = int(screen_width/5)
    p_y = int(screen_width/2)
    b_x = 0

    n_pip1 = get_Random_Pipes()
    n_pip2 = get_Random_Pipes()

    up_pips = [
        {'x':screen_width+200,'y':n_pip1[0]['y']},
        {'x':screen_width+200+(screen_width/2),'y':n_pip2[0]['y']},
    ]

    low_pips = [
        {'x':screen_width+200,'y':n_pip1[1]['y']},
        {'x':screen_width+200+(screen_width/2),'y':n_pip2[1]['y']},
    ]

    pip_Vx = -4
    p_vx = -9
    p_mvx = 10
    p_mvy = -8
    p_accuracy = 1

    p_flap_accuracy = -8
    p_flap = False

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if p_y > 0:
                    p_vx = p_flap_accuracy
                    p_flap = True
                    game_audio_sound['wing'].play()

            cr_test = is_Colliding(p_x,p_y,up_pips,low_pips)
            if cr_test:
                return

            p_middle_positions = p_x + game_image['player'].get_width()/2
            for pipe in up_pips:
                pip_middle_positions = pipe['x']+game_image['pipe'][0].get_width()/2
                if pip_middle_positions <= p_middle_positions < pip_middle_positions + 4:
                    score+=1
                    print(f"Your score is {score}")
                    game_audio_sound['point'].play()

            if p_vx < p_mvx and not p_flap:
                p_vx += p_accuracy

            if p_flap:
                p_flap = False
            p_height = game_image['player'].get_height()
            p_y = p_y + min(p_vx,play_area-p_y-p_height)

            for pip_upper,pip_lower in zip(up_pips,low_pips):
                pip_upper['x'] += pip_Vx
                pip_lower['x'] += pip_Vx

            if 0<up_pips[0]['x'] < 5:
                new_pip = get_Random_Pipes()
                up_pips.append(new_pip[0])
                low_pips.append(new_pip[1])

            if up_pips[0]['x'] < -game_image['pipe'][0].get_width():
                up_pips.pop(0)
                low_pips.pop(0)

            window.blit(game_image['background'],(0,0))
            for pip_upper,pip_lower in zip(up_pips,low_pips):
                window.blit(game_image['pip'][0], (pip_upper['x'],pip_upper['y']))
                window.blit(game_image['pip'][1], (pip_upper['x'],pip_upper['y']))

            window.blit(game_image['base'],(b_x,play_area))
            window.blit(game_image['player'],(p_x,p_y))
            d = [int(x) for x in list(str(score))]
            w=0
            for digit in d:
                w+=game_image['numbers'][digit].get_width()
            Xoffset = (screen_width-w)/2
            for digit in d:
                window.blit(game_image['numbers'][digit],(Xoffset,screen_height*0.12))
                Xoffset += game_image['numbers'][digit].get_width()

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

    ##game_image['message'] = pygame.image.load('images/message.png').convert_alpha()
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

