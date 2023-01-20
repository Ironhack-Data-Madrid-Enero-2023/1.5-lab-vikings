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
        return None

# Viking


class Viking(Soldier):
    def __init__ (self, name , health, strength ):

        self.health = health
        self.strength = strength

        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f'{self.name} has received {damage} points of damage')
        else:
            return ( f'{self.name} has died in act of combat')

    def battleCry(self):
        return f'Odin Owns You All!'



    

# Saxon


class Saxon(Soldier):

    def __init__ (self, health, strength):

        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'
    

    

  

# War


class War:
    def __init__(self):


        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:Viking):
        self.vikingArmy.append(viking)
        

    def addSaxon(self,saxon:Saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        lucha = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        else:
            pass

        return lucha


    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        lucha = viking.receiveDamage(saxon.strength)

        if viking.health <=0:
            self.vikingArmy.remove(viking)

        else:
            pass

        return lucha


    def showStatus(self):
        if len(self.saxonArmy)== 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy)== 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy)== 1 and len(self.vikingArmy)== 1:
            return 'Vikings and Saxons are still in the thick of battle.' 
        else:
            pass

        





