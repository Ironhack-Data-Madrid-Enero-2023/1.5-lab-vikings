import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, daño):
        if self.health <= 0:
            return True
        
        elif self.health > 0:
            self.health -= daño
       


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
         self.name = name
         Soldier.__init__(self, health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, daño):
        self.health = self.health - daño
        if self.health > 0:
            return (f"{self.name} has received {daño} points of damage") 
            
        
        else:
            return (f"{self.name} has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"

       
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def attack(self):
        return self.strength
        
    def receiveDamage(self, daño):
        self.health = self.health - daño
        if self.health > 0:
            return (f"A Saxon has received {daño} points of damage")
        
        else:
            return "A Saxon has died in combat"
    

# War


class War:
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        

        batalla = saxon.receiveDamage(viking.strength) 
           
        for muerto in self.saxonArmy:
            if muerto.health <= 0:
                self.saxonArmy.remove(muerto)


        return batalla
        

    def saxonAttack(self):

        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        batalla = viking.receiveDamage(saxon.strength) 
            
        for Muerto in self.vikingArmy:
            if Muerto.health <= 0:
                self.vikingArmy.remove(Muerto)
            


        return batalla         

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'

        elif len(self.saxonArmy) == 0:
            return  'Vikings have won the war of the century!'

        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'
