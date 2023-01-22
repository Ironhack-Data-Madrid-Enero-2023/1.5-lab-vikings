import random 
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength 
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage


# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage 
        if self.health > 0:
            return(f'{self.name} has received {damage} points of damage')
        else:
            return(f'{self.name} has died in act of combat')
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage 
        if self.health > 0:
            return(f"A Saxon has received {damage} points of damage")
        else:
            return(f"A Saxon has died in combat")
     

# War


class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    #Agregar Viking
    def addViking (self,Viking):
       self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
      self.saxonArmy.append(Saxon)
    #A `Saxon` (chosen at random) has their `receiveDamage()` method called with the damage equal to the `strength` of a `Viking` (also chosen at random)
    def vikingAttack(self):
        guerrero_v = random.choice(self.vikingArmy)
        guerrero_s = random.choice(self.saxonArmy)
        ataque = guerrero_s.receiveDamage(guerrero_v.attack()) 
        if guerrero_s.health <= 0:
            self.saxonArmy.remove(guerrero_s)
        return ataque 
    def saxonAttack(self):
        guerrero_v2 = random.choice(self.vikingArmy)
        guerrero_s2 = random.choice(self.saxonArmy)
        ataque2 = guerrero_v2.receiveDamage(guerrero_s2.attack()) 
        if guerrero_v2.health <= 0:
            self.vikingArmy.remove(guerrero_v2)
        return ataque2 

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return ("Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            return ("Saxons have fought for their lives and survive another day...")
        else:
            return("Vikings and Saxons are still in the thick of battle.")

