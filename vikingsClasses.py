
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength

    def receiveDamage (self,damage):
        self.health -= damage


# Viking


class Viking (Soldier):
    
    def __init__(self,name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

        
    def attack(self):
        return self.strength 

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0 : 
            return f"{self.name} has received {damage} points of damage"
        else:
            return f'{self.name} has died in act of combat'


    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
        
    def attack(self):
        
        return self.strength              

    def receiveDamage(self, damage):
        #self.damage = damage
        self.health -= damage 

        if self.health > 0 :
            return f"A Saxon has received {damage} points of damage"
        else :
            return "A Saxon has died in combat"

# War

from random import randint

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking): 
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack (self):
        x = len(self.saxonArmy)
        x = randint(0,x-1)

        y = len(self.vikingArmy)
        y = randint(0,y-1)

        a = self.saxonArmy[x].receiveDamage(self.vikingArmy[y].attack())
        
        if self.saxonArmy[x].health <= 0 :
            del self.saxonArmy[x]

        return a
        

    def saxonAttack(self):
        x = len(self.vikingArmy)
        x = randint(0,x-1)
        y = len(self.saxonArmy)
        y = randint(0,y-1)

        b = self.vikingArmy[x].receiveDamage(self.saxonArmy[y].attack()) 

        if self.vikingArmy[x].health <= 0 :
            del self.vikingArmy[x]

        return b

        
    def showStatus( self ):
        if len(self.saxonArmy) == 0 :
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0 :
            return "Saxons have fought for their lives and survive another day..."
        else:
            if len(self.vikingArmy) and len(self.saxonArmy) >=1 :
                return "Vikings and Saxons are still in the thick of battle."

                