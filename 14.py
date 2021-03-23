# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan, health=100, strength=1, agility=1, intelligence=1):
        self.name = name
        self.clan = clan
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def __repr__(self):
        return f"name: {self.name}, " \
               f"clan: {self.clan}, " \
               f"intelligence: {self.intelligence}, " \
               f"strength: {self.strength}, " \
               f"agility: {self.agility}"

    def heal(self):
        if self.health < 100:
            if self.health + 10 > 100:
                self.health = 100
            else:
                self.health += 10


class Mage(Unit):
    def __init__(self, name, clan, magic_type,  health=100, strength=1, agility=1, intelligence=1):
        super().__init__(name, clan, health, strength, agility, intelligence)
        self.magic_type = magic_type

    def __repr__(self):
        return "Mage: " + super().__repr__() + f", magic_type: {self.magic_type}"

    def increase(self):
        if self.intelligence < 10:
            self.intelligence += 1


class Archer(Unit):
    def __init__(self, name, clan, bow_type,  health=100, strength=1, agility=1, intelligence=1):
        super().__init__(name, clan, health, strength, agility, intelligence)
        self.bow_type = bow_type

    def __repr__(self):
        return "Archer: " + super().__repr__() + f", bow_type: {self.bow_type}"

    def increase(self):
        if self.agility < 10:
            self.agility += 1


class Knight(Unit):
    def __init__(self, name, clan, weapon_type,  health=100, strength=1, agility=1, intelligence=1):
        super().__init__(name, clan, health, strength, agility, intelligence)
        self.weapon_type = weapon_type

    def __repr__(self):
        return "Knight: " + super().__repr__() + f", weapon_type: {self.weapon_type}"

    def increase(self):
        if self.strength < 10:
            self.strength += 1


aragorn = Knight("Aragorn", "human", "long_sword")
aragorn.increase()
print(aragorn)

gendalf = Mage("Gendalf", "maiar",  "water")
gendalf.increase()
print(gendalf)

legolass = Archer("Legolas", "elf", "crossbow")
legolass.increase()
print(legolass)

