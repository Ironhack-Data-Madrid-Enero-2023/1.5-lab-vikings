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
        self.name = name
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
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
        self.health = self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'


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

        #Dos individuos cruzan miradas
        barbado = random.choice(self.vikingArmy)
        famelico = random.choice(self.saxonArmy)

        #Le sorrajan al sajón
        vergazo = famelico.receiveDamage(barbado.strength)

        #A chingar a su madre los sajones muertos
        for s in self.saxonArmy:
            if s.health <= 0:
                self.saxonArmy.remove(s)
        
        return vergazo



    def saxonAttack(self):

        #Dos individuos cruzan miradas
        barbado = random.choice(self.vikingArmy)
        famelico = random.choice(self.saxonArmy)

        #Le agreden al vikingo
        vergazo = barbado.receiveDamage(famelico.strength)

        #Se alargan las mesas del Valhalla
        for v in self.vikingArmy:
            if v.health <= 0:
                self.vikingArmy.remove(v)
        
        return vergazo
   
    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

