import random
# Soldier


class Soldier:
  def __init__(self, health, strength):
    self.health=health
    self.strength=strength

  def attack(self):
    return self.strength

  def receiveDamage(self, damage):
    self.damage=damage
    self.health=self.health - damage
    return



# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
         Soldier._init_(self,health,strength)

         name = self.name

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        if  self.health>0:
          return '{self.name} has received {damage} points of damage'
      
        else:

            self.health<0
            return('name has died in act of combat')
           
    def battleCry(self):
         return ('odin owns you all')

         




       

# Saxon


class Saxon(Soldier):
   def _init_(self,health,strength):
        Soldier.__init__(self, health, strength)

   def attack(self):
       return self.strength
   
   def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return 'A Saxon has received {damage} points of damage'
        else:
            return 'Saxon has died in combat'


# War


class War:
    def __init__(self):
    
         self.vikingArmy = []
         self.saxonArmy = []
    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)
        return
    def addSaxon(self,saxon: Saxon):
        self.vikingArmy.append(Saxon)
        return
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = self.receiveDamage(viking.strength)
        
    if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

    return result

    def showStatus(self):
        if len (self.saxonArmy) == 0:
           return ('Vikings have won the war of the century')
        if len (self.vikingArmy) ==0:
           return ( 'Saxons have fought for their lives and survive another day...') 
        else:
           return ('Vikings are Saxons are still in the thick of  battle')

