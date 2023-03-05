from random import randint

class Character():
    def __init__(self):
        self.attack = 5
        self.health = 100
        self.max_health = 100
        self.defense = 3
        self.alive = True
        self.name = '_error_!'

    def hit(self, amount=0):
        if amount:
            return amount
        else:
            dmg = randint(self.attack-2, self.attack+2)
            return max(dmg, 1)

    def get_damage(self, amount):
        dmg  = amount- self.defense
        self.health -= dmg
        print(f'{self.name} is hit for {dmg} damage! {self.health} HP left')
        if self.health <= 0:
            self.alive = False
            print(f'{self.name} is killed')

class Cave():
    def __init__(self, level):
        self.monsters = []
        self.level = level
        for i in range(randint(level*2, level*2 + 1)):
            type = randint(1,3)
            if type == 1:
                self.monsters.append(Cyclops())
            elif type == 2:
                self.monsters.append(Goblin())
            else:
                self.monsters.append(Gendalf())





class Goblin(Character):
    def __init__(self):
        super().__init__()
        self.attack = 2
        self.health = 120
        self.max_health = 120
        self.name = 'Goblin'
        self.exp = 40

class Gendalf(Character):
    def __init__(self):
        super().__init__()
        self.attack = 15
        self.health = 40
        self.max_health = 40
        self.name = 'Gendalf'
        self.exp = 45

class somebody(Character):
    def __init__(self):
        super().__init__()
        self.attack = 19
        self.health = 456
        self.max_health = 4560
        self.name = 'Gendalf'
        self.exp = 4567


class Cyclops(Character):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.max_health = 80
        self.name = 'Cyclops'
        self.exp = 35

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.attack = 15
        self.defense = 0
        self.health = 240
        self.max_health = 240
        self.name = 'Alex'
        self.level  = 0
        self.exp = 0
        self.exp_to_next =100

    def levelup(self):
        self.attack += 2
        self.defense += 1
        self.max_health += 20
        self.health = self.max_health
        self.level += 1
        self.exp = 0
        self.exp_to_next = self.level * 100


def mainloop():

    cyc1 = Cyclops()
    cyc2 = Cyclops()
    cyc3 = Cyclops()
    hero = Hero()
    goblin = Goblin()
    gendalf = Gendalf()

    lst = [Cave(1), Cave(2), Cave(3)]

    offerCave = 'Choose your cave:\n'
    for num, i in enumerate(lst):
        offerCave += f'{num}. Cave lvl {i.level}\n'
    choice = int(input(offerCave))

    monsters = lst[choice].monsters

    while hero.alive and len(monsters) > 0:
        offer = 'Choose your target:\n'
        for num, m in enumerate(monsters):
            offer += f'{num}.{m.name} ({m.health}/{m.max_health})\n'

        number = int(input(offer))
        monsters[number].get_damage(hero.hit())

        if not monsters[number].alive:
            hero.exp += monsters[number].exp
            print('Your exp:', hero.exp)
            if hero.exp > hero.exp_to_next:
                hero.levelup()
                print('Health: ', hero.max_health, 'Your level', hero.level)

        monsters = [i for i in monsters if i.alive == True]
        for m in monsters:
            hero.get_damage(m.hit())

        if not hero.alive:
            print('You are dead!')
            break

    if hero.alive:
        print('You won!')

mainloop()