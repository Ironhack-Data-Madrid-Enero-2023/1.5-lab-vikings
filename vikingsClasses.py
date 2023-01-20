
# Soldier
from random import randint

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War


class War():

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        saxonNumber = randint(0,(len(self.saxonArmy)-1))
        vikingNumber = randint(0, (len(self.vikingArmy)-1))

        a = self.saxonArmy[saxonNumber].receiveDamage(self.vikingArmy[vikingNumber].attack())

        if self.saxonArmy[saxonNumber].health < 1:
            self.saxonArmy.pop(saxonNumber)
        
        return a
    
    def saxonAttack(self):
        saxonNumber = randint(0,(len(self.saxonArmy)-1))
        vikingNumber = randint(0, (len(self.vikingArmy)-1))

        b = self.vikingArmy[vikingNumber].receiveDamage(self.saxonArmy[saxonNumber].attack())

        if self.vikingArmy[vikingNumber].health < 1:
            self.vikingArmy.pop(vikingNumber)
        
        return b

    def showStatus(self):
        if len(self.saxonArmy) < 1:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) < 1:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) > 0 & len(self.vikingArmy):
            return "Vikings and Saxons are still in the thick of battle."


