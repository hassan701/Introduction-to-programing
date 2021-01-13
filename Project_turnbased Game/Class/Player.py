from settings import *
import random


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y,name,level=1):
        self.Name = name  # Basic Name
        self.Type = "Player"  # Monster(Wood,Fire,Water,Fly)/Player/Undead
        self.Level = level
        self.MaxHP = 10  # Max HIt piont
        self.HP = 10  # HIt piont
        self.AC = 14  # Arrmor class
        self.NormalAC = self.AC
        self.ACTemp = self.AC + 2
        self.AC = 14
        self.Speed = 10  # Initiative
        self.BasicAttack = 5
        self.turn = False
        ###
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.transform.scale(game.player_img[0],(64,64))
        self.rect = self.image.get_rect()
        self.vx,self.vy = 0,0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def Level_UP(self):
        self.Level = self.Level +1
        self.MaxHP = (5 *(self.Level+1)) + random.randint(0,3)
        self.HP = self.MaxHP
        self.AC = self.AC +(self.Level//2) if self.AC<18 else self.AC
        self.Speed = 10 + (self.Level//2)
        self.BasicAttack = self.BasicAttack * self.Level//2 +random.randint(1,3)

    def Attack(self,Target):
        if Target.HP != 0:
            print("Monster Alive")
            if random.randint(1,20) >= Target.AC:
                print("Attack hits")
                Min_damage = self.BasicAttack - int(self.BasicAttack * 0.2)
                Max_damage = self.BasicAttack
                Damage = random.randint(Min_damage, Max_damage)
                if Target.HP >= Damage:
                    Target.HP = Target.HP - Damage
                else:
                    Target.HP = 0
                print("Monster Health",Target.HP)
            else:
                print("Attack Misses")
    def Defence(self):
        print("Defence")
        self.ACTemp = self.AC +2
        self.NormalACAC = self.ACTemp
        print(self.AC,"-->",self.ACTemp)


    def update(self):
        if not self.game.AttackMode:
            self.get_keys()
            self.x += self.vx * self.game.dt
            self.y += self.vy * self.game.dt
            self.rect.topleft = (self.x,self.y)
            if pg.sprite.spritecollideany(self, self.game.walls):
                self.x -= self.vx * self.game.dt
                self.y -= self.vy * self.game.dt
                self.rect.topleft = (self.x, self.y)

