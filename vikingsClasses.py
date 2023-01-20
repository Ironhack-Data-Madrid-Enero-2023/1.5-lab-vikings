
import random


# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength


    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        self.health = self.health - damage

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):

        Soldier.__init__(self, health, strength)

        self.name = name

    def receiveDamage(self, damage):

        self.health = self.health - damage

        if self.health > 0:
            return(f'{self.name} has received {damage} points of damage')

        else:
            return(f'{self.name} has died in act of combat')

    def battleCry(self):

        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):

        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):

        self.health = self.health - damage

        if self.health > 0:
            return(f'A Saxon has received {damage} points of damage')

        else:
            return(f'A Saxon has died in combat')

# War


class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):

        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):

        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

        random_vik = random.choice(self.vikingArmy)
        random_sax = random.choice(self.saxonArmy)

        dmg_rec_sax = random_sax.receiveDamage(random_vik.strength)

        if random_sax.health <= 0:

            self.saxonArmy.remove(random_sax)

        else:
            pass

        return dmg_rec_sax

    def saxonAttack(self):   

        random_vik = random.choice(self.vikingArmy)
        random_sax = random.choice(self.saxonArmy)

        dmg_rec_vik = random_vik.receiveDamage(random_sax.strength)
        
        if random_vik.health <= 0:

            self.vikingArmy.remove(random_vik) 

        else:
            pass

        return dmg_rec_vik

    def showStatus(self):

        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        else:
            return 'Vikings and Saxons are still in the thick of battle.'

    





    

        


