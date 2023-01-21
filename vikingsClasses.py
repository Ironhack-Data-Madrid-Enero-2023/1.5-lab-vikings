import random

class Soldier:

    def __init__(self, health, strength):

        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

class Viking(Soldier):

    def __init__(self, name, health, strength):
        
        Soldier.__init__(self, health, strength)
        self.name=name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return "Odin Owns You All!"
        

class Saxon(Soldier):
    def __init__(self,health,strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'    


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        rs = random.choice(self.saxonArmy)
        rv = random.choice(self.vikingArmy)

        dam = rs.receiveDamage(rv.strength)

        if rs.health <= 0:
            self.saxonArmy.remove(rs)

        return dam
    
    def saxonAttack(self):
        rs = random.choice(self.saxonArmy)
        rv = random.choice(self.vikingArmy)

        dam = rv.receiveDamage(rs.strength)

        if rv.health <= 0:
            self.vikingArmy.remove(rv)

        return dam
    
    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
        

