import pygame, sys
from pygame.locals import *
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Project')
screen = pygame.display.set_mode((500, 500), 0, 50)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)


click = False


def main_menu():
    click = False
    while True:

        screen.fill((0, 0, 0))
        draw_text('Main Menu', font, (255, 255, 255), 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                Newgame()
        if button_2.collidepoint((mx, my)):
            if click:
                Options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

def Newgame():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('New Game', font, (255, 255, 255), 20, 20)

        Exit()
        pygame.display.update()
        mainClock.tick(60)

def Options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Options', font, (255, 255, 255), 20, 20)

        Exit()
        pygame.display.update()
        mainClock.tick(60)

main_menu()