import pygame as pg
pg.init()
import sys
from Class import Game
from settings import *
class Menu():
    def __init__(self):
        self.WIDTH= 800  # 960#1024   # 16 * 64 or 32 * 32 or 64 * 16
        self.HEIGHT = 600  # 720#768  # 16 * 48 or 32 * 24 or 64 * 12
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.run_display = True
        self.score=[]
        self.volume_Music = 0.5
        self.volume_Sound = 0.5
    def events(self):
        WIDTH =self.WIDTH
        HEIGHT = self.HEIGHT
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0] and self.MainMenu_on == True:
                    pos =pg.mouse.get_pos()
                    if (pos[0]>(WIDTH/ 2)-57 and pos[0]<(WIDTH/2)+57):
                        print("here")
                        if (pos[1] > (HEIGHT/ 2-100)-18and pos[1] < (HEIGHT/ 2-100)+18):
                            print("New Game")
                            self.NewGame()
                        elif(pos[1] > (HEIGHT/ 2)-18 and pos[1] < (HEIGHT/ 2)+18):
                            print("Options")
                            self.Options_on = True
                            self.Options()
                        elif(pos[1] > (HEIGHT/ 2+100)-18 and pos[1] < (HEIGHT/ 2+100)+18):
                            print("Quit")
                            quit()
                if self.Options_on== True and pg.mouse.get_pressed()[0]:
                        pos =pg.mouse.get_pos()
                        if (pos[1]>(HEIGHT/2-100) - 12 and pos[1] < (HEIGHT/2-100) + 12):
                            if (pos[0] > ((WIDTH / 2) - (WIDTH/12)*3)-12and pos[0] < ((WIDTH / 2) - (WIDTH/12)*3) +12):
                                if self.volume_Music > 0:
                                    self.volume_Music = round(self.volume_Music - 0.1,1)
                            elif(pos[0] > ((WIDTH / 2) - (WIDTH/12)*2)-12 and pos[0] < ((WIDTH / 2) - (WIDTH/12)*2) +12):
                                pass
                            elif(pos[0] > ((WIDTH / 2) - (WIDTH/12)*1)-12 and pos[0] < ((WIDTH / 2) - (WIDTH/12)*1) +12):
                                if self.volume_Music < 1:
                                    self.volume_Music =round(self.volume_Music + 0.1,1)

                        if (pos[1]>(HEIGHT/2-200) - 12 and pos[1] < (HEIGHT/2-200) + 12):
                            if (pos[0] > ((WIDTH / 2) - (WIDTH/12)*3)-12and pos[0] < ((WIDTH / 2) - (WIDTH/12)*3) +12):
                                if self.volume_Sound > 0:
                                    self.volume_Sound = round(self.volume_Sound + 0.1,1)
                            elif(pos[0] > ((WIDTH / 2) - (WIDTH/12)*2)-12 and pos[0] < ((WIDTH / 2) - (WIDTH/12)*2) +12):
                                pass
                            elif(pos[0] > ((WIDTH / 2) - (WIDTH/12)*1)-12 and pos[0] < ((WIDTH / 2) - (WIDTH/12)*1) +12):
                                if self.volume_Sound < 1:
                                    self.volume_Sound =round(self.volume_Sound + 0.1,1)

            if event.type == pg.KEYDOWN and self.MainMenu_on == False:
                print("key")
                if event.key == pg.K_BACKSPACE:
                    self.MainMenu()


    def quit(self):
        pg.quit()
        sys.exit()

    def MainMenu(self):
            self.MainMenu_on = True
            self.Options_on = False
            img_folder = path.join(game_folder, 'Assets/Background')
            Music_folder = path.join(game_folder, 'Assets/Music')
            pg.mixer.music.load(path.join(Music_folder, Menu_Music))
            pg.mixer.music.set_volume(self.volume_Music)
            with open(path.join(game_folder, 'files\\Highscore.txt')) as Score_file:
                file = Score_file.read().split('\n')
                for line in file:
                    self.score.append(int(line))
            Score_file.close()
            self.score.sort()
            self.score.reverse()

            pg.mixer.music.play(loops=-1)
            while self.MainMenu_on == True:
                pg.mixer.music.set_volume(self.volume_Music)
                self.events()
                self.Menu_img = pg.image.load(path.join(img_folder, 'Background.jpg')).convert_alpha()
                self.Menu_img = pg.transform.scale(self.Menu_img, (WIDTH, HEIGHT))
                self.screen.blit(self.Menu_img, (0, 0))
                self.draw_text('NEW GAME', 20, WIDTH/ 2, HEIGHT/ 2-100)
                self.draw_text('Options', 20, WIDTH / 2, HEIGHT / 2)
                self.draw_text('Quit', 20, WIDTH / 2, HEIGHT / 2+100)
                self.draw_text('HIGHEST SCORE:', 20, WIDTH / 2-300, HEIGHT / 2 - 250)
                self.draw_text("1st: "+str(self.score[0]), 20, WIDTH / 2-300, HEIGHT / 2 - 200)
                self.draw_text("2nd: "+str(self.score[1]), 20, WIDTH / 2-300, HEIGHT / 2 - 150)
                self.draw_text("3rd: "+str(self.score[2]), 20, WIDTH / 2-300, HEIGHT / 2 - 100)

                pg.display.update()

    def NewGame(self):
            self.MainMenu_on = False
            self.screen.fill(BLACK)
            pg.display.update()
            Game.gameON(self.volume_Music, self.volume_Music)
    def Options(self):
        self.MainMenu_on = False
        self.Options_on = True
        while self.Options_on:
            pg.mixer.music.set_volume(self.volume_Music)

            self.events()
            self.screen.blit(self.Menu_img, (0, 0))
            self.draw_text('Music:', 15, (WIDTH / 2)-(WIDTH/12)*4.5, HEIGHT / 2 - 100)
            self.draw_text('-', 15, (WIDTH / 2) - (WIDTH/12)*3, HEIGHT / 2 - 100)
            self.draw_text(str((self.volume_Music*100)), 15, (WIDTH / 2) - (WIDTH/12)*2, HEIGHT / 2 - 100)
            self.draw_text('+', 15, (WIDTH / 2) - (WIDTH/12)*1, HEIGHT / 2 - 100)

            self.draw_text('Sounds:', 15, (WIDTH / 2) - (WIDTH / 12) * 4.5, HEIGHT / 2 - 200)
            self.draw_text('-', 15, (WIDTH / 2) - (WIDTH / 12) * 3, HEIGHT / 2 - 200)
            self.draw_text(str((self.volume_Sound*100)), 15, (WIDTH / 2) - (WIDTH / 12) * 2, HEIGHT / 2 - 200)
            self.draw_text('+', 15, (WIDTH / 2) - (WIDTH / 12) * 1, HEIGHT / 2 - 200)
            pg.display.update()


    def draw_text(self, text, size, x, y):
        self.font_name = pg.font.get_default_font()
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
g = Menu()
while True:
    g.MainMenu()