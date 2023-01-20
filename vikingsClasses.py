
import random
# Soldier


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
        self.name = name
        Soldier.__init__(self, health, strength)
    def receiveDamage (self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f'A Saxon has received {damage} points of damage')
        else:
            return ('A Saxon has died in combat')
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:Viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon:Saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)

        fight = sax.receiveDamage(vik.strength)

        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return fight

    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)

        fight = vik.receiveDamage(sax.strength)

        if vik.health <= 0:
            self.vikingArmy.remove(vik)

        return fight

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return ('Vikings have won the war of the century!')
        elif len(self.vikingArmy) == 0:
            return ('Saxons have fought for their lives and survive another day...')
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return ('Vikings and Saxons are still in the thick of battle.')
        else:
            pass