import pygame as pg
from os import path

# define some colors (R, G, B)
game_folder = path.dirname(__file__)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# game settings
WIDTH = 800#960#1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600#720#768  # 16 * 48 or 32 * 24 or 64 * 12


FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = int(WIDTH / TILESIZE)
GRIDHEIGHT = int(HEIGHT / TILESIZE)

PLAYER_SPEED = 150
#Maps
Map_txt=['map1.txt','map2.txt']

#Images
PLAYER_IMG= 'Player_idle.png'
PLAYER_IMG2= 'Player_attack.png'
Monsters_img = ['Dragon.png','Rock_golem.png', 'Skeleton.png','SLime_lizard.png', 'Tree_Wolf.png', 'VineMAN.png', 'Zombie_wolf.png']

floor_tile = "Tile_floor.jpg"
wall_tile = 'Wall_tile.jpg'
Portal_tile = 'Portal.png'

#Music
Menu_Music = "bensound-memories.ogg"
Game_Music = "bensound-creativeminds.ogg"
#sound effects
SOUND_EFFECTS = {'Level UP':'Level-Up-Sound-Effect-YouTube.wav','MonsterAttack':'Monster-Growl-Sound-Effect-YouTube.wav',
                 'PlayerAttack':'Sword-Slash-Attack-Sound-Effect-YouTube.wav',"Go_Portal":'The-Portal-SOUND-Effect-YouTube.wav',
                 'DEATH':'Dark-Souls-_-You-Died-_-Sound-Effect-YouTube.wav'}
"""
Level_se = 'Level Up Sound Effect - YouTube.wav'
Level_se = 'Level Up Sound Effect - YouTube.wav'
Growl_se = 'Monster-Growl-Sound-Effect-YouTube.wav'
Sword_se = 'Sword-Slash-Attack-Sound-Effect-YouTube.wav'
portal_se = 'The-Portal-SOUND-Effect-YouTube.wav'
Death_se = 'Dark-Souls-_-You-Died-_-Sound-Effect-YouTube.wav'"""




class Map:
    def __init__(self, filename):
        self.map_data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.map_data.append(line.strip())

        self.tileWidth = len(self.map_data[0])
        self.tileHeigth = len(self.map_data)
        self.width = self.tileWidth * TILESIZE
        self.height = self.tileHeigth * TILESIZE

class Camera:
    def __init__(self,height,width):
        self.camera = pg.Rect(0,0,width,height)
        self.width = width
        self.height = height
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    def update(self,target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT / 2)
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.height - WIDTH), x)
        y = max(-(self.width - HEIGHT), y)
        self.camera = pg.Rect(x,y,self.width,self.height)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_tile
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE