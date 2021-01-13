import random
from settings import *

class Event(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.MonsterEvent
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.Portal_tile
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        if pg.sprite.spritecollideany(self, self.game.players):
            self.kill()
            self.game.player.x -= self.x
            self.game.player.x -= self.y
            self.game.player.rect.topleft = (self.x, self.y)
            self.game.Battle()

class Monster(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.monsters
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.turn = False
    def CreateMonster(self,level):
        monster = []
        with open(path.join(game_folder,'files\\Monsters.txt')) as Monster_file:
            file = Monster_file.read().split('\n')
            for line in file:
                monster.append(line)
        i = random.randint(0,1)
        monster = monster[i].split(',')
        Monster_file.close()
        self.Name = str(monster[0])
        self.Type = str(monster[1])
        self.picture = int(monster[2])
        self.challegerLevel = random.randint(level-1,level)
        self.MaxHP = 5*level
        self.HP = self.MaxHP
        self.AC = 13 +(self.challegerLevel//2)
        self.Mana = (5*self.challegerLevel)
        self.Speed = (5.5*self.challegerLevel) if self.Type=='Grass' else (5*self.challegerLevel)
        self.ALL_moveset = self.Movesets()
        self.Attacks = self.Attackset()
    def Movesets(self):
        moveset= {}
        with open(path.join(game_folder,'files\\Moves.txt')) as Moves_file:
            file = Moves_file.read().split('\n')
            for line in file:
                m = line.split(';')
                moveset[m[0]] = m[1]

        return moveset
    def Attackset(self):
        attack = []
        for M in self.ALL_moveset:
            s = self.ALL_moveset.get(M)
            Move= s.split(',')
            if Move[0] == str(self.Type) and Move[1] <= str(self.challegerLevel):
                attack.append(M)
        return attack

    def Attack(self,Target):
        if Target.HP != 0 and self.HP >0:
            print("Target Alive")
            print("Attacking")
            if random.randint(1,20) >= Target.NormalAC:
                print("Attack Hit")
                if Target.HP > 10 and self.Mana > 0:
                    print("Using magic")
                    self.Attacks.reverse()
                    for line in self.Attacks:
                        m = self.ALL_moveset.get(line)
                        Move = m.split(',')
                        if self.Mana >= int(Move[2]):
                            print("Using",line)
                            Min_damage =int(Move[3])//2* self.challegerLevel//2
                            Max_damage =int(Move[3])* self.challegerLevel//2
                            Damage = random.randint(Min_damage, Max_damage)
                            if Target.HP >= Damage:
                                Target.HP = Target.HP - Damage
                            else:
                                Target.HP = 0
                            print('Player Health', Target.HP,"Damge done",Damage)
                            break
                else:
                    print("Using basic attack")
                    m = self.ALL_moveset.get('Slash')
                    Move = m.split(',')
                    Min_damage = 1
                    Max_damage = int(Move[3])
                    Damage= random.randint(Min_damage, Max_damage)
                    if Target.HP >= Damage:
                        Target.HP = Target.HP - Damage
                    else:
                        Target.HP = 0
                    print('Player Health',Target.HP,'Damage',Damage)
            else:
                print("Attack Misses")


    def update(self):
        pass

