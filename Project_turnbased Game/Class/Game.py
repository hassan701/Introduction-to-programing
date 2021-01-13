import sys
from Class.Monster import Monster
from Class.Monster import Event
from Class import Player
from settings import *
import random
import pygame as pg


class Game:
    def __init__(self,volume_Music,volume_Sound):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.FPS = FPS
        pg.key.set_repeat(500, 100)
        self.Image_mode = 0
        self.Monster_Image_mode = 200
        self.volume_Music = volume_Music
        self.volume_Sound = volume_Sound
        self.load_data(self.volume_Music,self.volume_Sound)
        self.font_name = pg.font.get_default_font()

    def load_data(self,volume_Music,volume_Sound):
        game_folder = path.dirname(__file__)
        Map_folder = (path.join(game_folder, '../files/Maps'))
        Player_img_folder = path.join(game_folder, '../Assets/Player')
        Music_folder = path.join(game_folder, '../Assets/Music')
        SF_folder = path.join(game_folder, '../Assets/Sound effects')
        Background_img_folder = path.join(game_folder, '../Assets/Background')
        Tile_img_folder = path.join(game_folder, '../Assets/Tile')
        self.Menu_img = pg.image.load(path.join(Background_img_folder, 'Background2.jpg')).convert_alpha()
        self.Menu_img = pg.transform.scale(self.Menu_img, (WIDTH, HEIGHT))
        self.map = Map(path.join(Map_folder, Map_txt[random.randint(0,1)]))
        self.wall_tile = pg.image.load(path.join(Tile_img_folder, wall_tile)).convert_alpha()
        self.Portal_tile = pg.image.load(path.join(Tile_img_folder, Portal_tile)).convert_alpha()
        self.wall_tile = pg.transform.scale(self.wall_tile, (TILESIZE, TILESIZE))
        self.floor_tile = pg.image.load(path.join(Tile_img_folder, floor_tile)).convert_alpha()
        self.floor_tile = pg.transform.scale(self.floor_tile, (TILESIZE, TILESIZE))
        self.player_img = [pg.image.load(path.join(Player_img_folder, PLAYER_IMG)).convert_alpha(),pg.image.load(path.join(Player_img_folder, PLAYER_IMG2)).convert_alpha()]

        #Music
        pg.mixer.music.load(path.join(Music_folder, Game_Music))
        pg.mixer.music.set_volume(volume_Music)
        #Sound Effects
        pg.mixer.music.set_volume(volume_Sound)
        self.sound = {}
        for s in SOUND_EFFECTS:
            self.sound[s] =pg.mixer.Sound(path.join(SF_folder,SOUND_EFFECTS[s]))


    def new(self):
        # Setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.pionts_goal = 0
        self.MonsterEvent = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.monsters = pg.sprite.Group()
        for row, tiles in enumerate(self.map.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player.Player(self, col, row,"Rick")
                if tile == 'M':
                    self.pionts_goal = self.pionts_goal +1
                    Event(self, col, row)
        self.camera = Camera(self.map.width,self.map.height)

    def run(self,level):
        # game loop
        self.playing = True
        self.AttackMode = False
        self.LevelCleared = False
        self.Menu = False
        pg.mixer.music.play(loops=-1)
        if level >0:
            for i in range(level):
                self.player.Level_UP()
        while self.playing:
            self.dt = self.clock.tick(self.FPS)/1000
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()
    def update(self):
        # update the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        pg.mixer.music.set_volume(self.volume_Music)
        pg.mixer.music.set_volume(self.volume_Sound)
        if self.AttackMode:
            pg.mixer.music.set_volume(0)
            self.Fight()

    def draw_grid(self):
        #used for testing,not need anymore
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def gg(self):
        #Game over screen
        pg.mixer.music.stop()
        self.screen.fill(BLACK)
        self.draw_text('YOU DIED', 20, WIDTH//2, HEIGHT//2)
        self.sound['DEATH'].play()
        with open(path.join(game_folder, 'files\\Highscore.txt'),'a+') as Score_file:
            file = Score_file.write("\n"+str(self.player.Level))
        Score_file.close()
        pg.display.flip()
        pg.time.wait(2000)

    def ggez(self):
        # Winning screen
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, '../Assets/Background')
        self.Menu_img = pg.image.load(path.join(img_folder, 'Background2.jpg')).convert_alpha()
        self.Menu_img = pg.transform.scale(self.Menu_img, (WIDTH, HEIGHT))
        self.screen.blit(self.Menu_img, (0, 0))
        self.draw_text('YOU DELVE DEEPER', 20, WIDTH//2, HEIGHT//2-100)
        self.draw_text('LEVEL UP!', 20, WIDTH // 2, HEIGHT // 2)
        pg.display.flip()
        pg.time.wait(1000)




    def draw(self):
        if not self.AttackMode:
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
            self.screen.fill(BGCOLOR)
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            self.draw_BAR(self.screen, 10, 10, (self.player.HP / self.player.MaxHP))
            self.draw_text('Level:'+str(self.player.Level), 20, 45, 45)

            pg.display.flip()
        if self.AttackMode:
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
            self.screen.fill(BLACK)
            self.screen.blit(self.Menu_img, (0, 0))
            self.draw_BAR(self.screen, 10, 10, (self.player.HP / self.player.MaxHP))
            self.draw_BAR(self.screen, WIDTH-120, 10, (self.monster.HP / self.monster.MaxHP))
            self.draw_text('Monster Level:' + str(self.monster.challegerLevel), 15, WIDTH-70, 40)
            self.screen.blit(self.player_img[self.Image_mode], (WIDTH/2-200, HEIGHT/2))
            self.screen.blit(self.monster_img, (WIDTH / 2 + self.Monster_Image_mode, HEIGHT / 2))
            pg.display.flip()

    def draw_text(self, text, size, x, y):
        #show text on the screen
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
    def draw_BAR(self,surface, x, y, pct):
        #show health bar
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surface, col, fill_rect)
        pg.draw.rect(surface, WHITE, outline_rect, 2)

    def events(self):
        #catch userimput during game runtime
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_m:
                    print("Works")
                    self.Menu = True
                    self.playing = False
    def Battle(self):
        #Generate the monster
        self.timer = 0;
        self.sound['Go_Portal'].play()
        self.AttackMode = True
        self.lastturn = ''
        keys = pg.key.get_pressed()
        self.monster= Monster(self,WIDTH/2, HEIGHT/2)
        self.monster.CreateMonster(self.player.Level)
        print(self.monster.Name,self.monster.Type,self.monster.HP,self.monster.AC,self.monster.Attacks)
        game_folder = path.dirname(__file__)
        Monsters_img_folder = path.join(game_folder, '../Assets/Monsters')
        self.monster_img = pg.image.load(path.join(Monsters_img_folder, Monsters_img[self.monster.picture])).convert_alpha()
        print("Player",self.player.HP )
        if self.monster.Speed < self.player.Speed:
            self.player.turn= True
            self.monster.turn = False
        elif self.monster.Speed > self.player.Speed:
            self.monster.turn = True
            self.player.turn = False
        else:
            self.player.turn = True
            self.monster.turn = False
        pg.time.wait(1000)
        self.sound['Go_Portal'].stop()
    def Fight(self):
        #Turn based logic
        keys = pg.key.get_pressed()
        if self.player.HP > 0 and self.monster.HP > 0:
            if self.player.turn:
                self.Image_mode = 0
                if keys[pg.K_f]:
                    self.player.NormalAC = self.player.AC
                    self.player.Attack(self.monster)
                    self.Image_mode = 1
                    self.sound['MonsterAttack'].stop()
                    self.sound['PlayerAttack'].play()
                    self.lastturn = "Player"
                    print(self.player.NormalAC)
                    self.timer =0
                    self.player.turn = False
                if keys[pg.K_r]:
                    self.player.Defence()
                    self.Image_mode = 0
                    self.sound['MonsterAttack'].stop()
                    self.lastturn = "Player"
                    self.timer =0
                    self.player.turn = False

            elif self.player.turn == False and self.monster.turn== False:
                time =pg.time.get_ticks()/1000
                self.timer= self.timer + 1
                if self.timer >= 50:
                    print("Works")
                    if self.lastturn == "Player":
                        self.Image_mode = 0
                        self.sound['PlayerAttack'].stop()
                        self.monster.turn = True
                    elif self.lastturn == "Monster":
                        self.Monster_Image_mode = 100
                        self.sound['MonsterAttack'].stop()
                        self.player.turn = True

            elif self.monster.turn:
                print("Monster turn")
                self.monster.Attack(self.player)
                self.Monster_Image_mode = 0
                self.sound['PlayerAttack'].stop()
                self.sound['MonsterAttack'].play()
                print("Monster turn OVer")
                self.timer =0
                self.lastturn = "Monster"
                self.monster.turn = False
        elif self.player.HP == 0 or self.monster.HP == 0:
            if self.player.HP >0:
                self.sound['PlayerAttack'].stop()
                self.sound['MonsterAttack'].stop()
                print("Monster defeated")
                self.pionts_goal= self.pionts_goal -1
                if self.pionts_goal ==0:
                    print("Level CLeared")
                    self.sound['Level UP'].play()
                    self.LevelCleared = True
                    self.playing = False
                self.AttackMode = False
            else:
                print("Game over")
                self.sound['PlayerAttack'].stop()
                self.sound['MonsterAttack'].stop()
                self.AttackMode = False
                self.playing = False



def gameON(volume_Music,volume_Sound):
    GameRuning= True
    g = Game(volume_Music,volume_Sound)
    level = 0
    while True:
        g.new()
        g.run(level)
        if not g.LevelCleared:
            if not g.Menu:
                g.gg()
            break
        else:
            g.ggez()
            level = level +1

