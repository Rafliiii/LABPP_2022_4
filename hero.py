class Human:
    def __init__(self, name, position):
        self.name = name
        self.__pos_x = position

    def setMovement(self, move):
        if move == 'L':
            self.__pos_x -= self._speed
        if move == 'R':
            self.__pos_x += self._speed 


class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self.health = health
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.health -= self._power

    def getHealth(self):
        return self.health 

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._armor = 26
        self._power = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target.health -= self._power

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        target.health -= self._power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self.health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target.health += 150

health = int(input())