class Monster():
    def __init__(self, hp) -> None:
        self.hp = hp
        self.alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def checkStatus(self):
        if self.alive: print('살아있습니다.')
        else: print('죽었습니다.')


m = Monster(100)
m.damage(120)

m2 = Monster(100)
m2.damage(90)

m.checkStatus()
m2.checkStatus()