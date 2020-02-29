import pygame
import time
import random
import sys
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()
display_width = 800
display_height = 1000
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dred = (150, 0, 0)
green = (0, 255, 0)
dgreen = (0, 150, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kapitan Bomba: Zemsta Dupy')
tlo = pygame.image.load('kosmos.png')
carImg = pygame.image.load('orzel.png')
planet = pygame.image.load('planet.png')
car_width = 71
car_height = 200
planet_width = 100
planet_height = 91

crash_s = pygame.mixer.Sound('fail.wav')


# menu_m = pygame.mixer.music.load("menu.mp3")
# game_m = pygame.mixer.music.load('gra.wav')

def score(dodged):
    font = pygame.font.SysFont(None, 40)
    text = font.render("PUNKTY: " + str(dodged), True, white)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, ):
    # pygame.draw.rect(gameDisplay, green, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(planet, (thingx, thingy))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, size, color, tx, ty):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (tx, ty)
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_s)
    message_display('Tępy huj!', 100, red, (display_width / 2), (display_height / 2))
    time.sleep(3)
    game_intro()


def game_intro():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('menu.mp3')
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        gameDisplay.blit(tlo, (0, 0))
        message_display('Kapitan Bomba:', 100, white, (display_width / 2), (display_height / 2 - 300))
        message_display('Zemsta Dupy', 100, white, (display_width / 2), (display_height / 2 - 200))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 < mouse[0] < 650 and 400 < mouse[1] < 600:
            pygame.draw.rect(gameDisplay, green, ((display_width / 2 - 250), (display_height / 2 - 100), 500, 200))
            message_display('GRAJ', 100, black, (display_width / 2), 500)
        else:
            pygame.draw.rect(gameDisplay, dgreen, ((display_width / 2 - 250), (display_height / 2 - 100), 500, 200))
            message_display('GRAJ', 100, black, (display_width / 2), 500)
        if 150 < mouse[0] < 650 and 610 < mouse[1] < 810:
            pygame.draw.rect(gameDisplay, red, ((display_width / 2 - 250), (display_height / 2 + 110), 500, 200))
            message_display('NIE GRAJ', 100, black, (display_width / 2), 710)
        else:
            pygame.draw.rect(gameDisplay, dred, ((display_width / 2 - 250), (display_height / 2 + 110), 500, 200))
            message_display('NIE GRAJ', 100, black, (display_width / 2), 710)

        if 150 < mouse[0] < 650 and 400 < mouse[1] < 600 and click[0] == 1:
            game_loop()
        if 150 < mouse[0] < 650 and 610 < mouse[1] < 810 and click[0] == 1:
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)


def game_loop():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('gra.wav')
    pygame.mixer.music.play(-1)
    x = (400 - car_width / 2)
    y = (1000 - car_height)
    x_change = 0

    thingx = random.randrange(0, display_width - 100)
    thingy = -600
    thing_speed = 10
    thing_width, thing_height = 100, 91
    dodged = 0
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8
                elif event.key == pygame.K_d:
                    x_change = 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
        gameDisplay.blit(tlo, (0, 0))
        things(thingx, thingy, thing_width, thing_height, )
        thingy += thing_speed

        car(x, y)
        score(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        if thingy > display_height:
            thingy = 0 - thing_height
            thingx = random.randrange(0, display_width - 100)
            dodged += 1
            if dodged % 10 == 0:
                thing_speed += 1

        if (y < thingy + thing_height) and (
                thingx < x < thingx + thing_width or thingx < x + car_width < thingx + thing_width):
            crash()
        pygame.display.update()
        clock.tick(100)


game_intro()
game_loop()
