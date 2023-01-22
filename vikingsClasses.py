
# Soldier


class Soldier:
    # metodo constructor, donde estan los atributos
    def __init__(self, health, strength):
        #atributos
        self.health=health
        self.strength=strength
    #métodos (attack y receive damage)
    def attack(self):
        #definimos la función attack; decimos que  si la salud es mayor que 0, retorne el valor de la fuerza del soldado.
        if self.health > 0:
            return self.strength
        
    def receiveDamage(self, damage):
        #definimos la función receiveDamage, tomando un argumento que es el damage; 
        self.health -= damage 

# Viking


class Viking(Soldier): #clase hija, hereda de la clase Soldier
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        #atributos: los que emanan de Soldier, más uno nuevo llamado name
        self.name=name
        #métodos: attack (no necesita reimplementación) y receiveDamage (sí necesita reimp.) heredados de Soldier y battleCry.
    def receiveDamage(self, damage):
            self.health -= damage
            if self.health > 0:
                return f"{self.name} has received {damage} points of damage"
            else:
                return f"{self.name} has died in act of combat"
    def battleCry(self):
            return f"Odin Owns You All!"


# Saxon


class Saxon(Soldier): #clase hija, hereda de la clase Soldier
    def __init__(self, health, strength):
        super().__init__(health, strength)
        #atributos: los que emanan de Soldier, no hay ninguno nuevo.
        #métodos: attack, que no necesita reimplementación y receiveDamage que sí.
    def receiveDamage(self, damage):
            self.health -= damage
            if self.health > 0:
                return f"A Saxon has received {damage} points of damage"
            else:
                return f"A Saxon has died in combat"

# War


class War:
    # metodo constructor, donde estan los atributos
    def __init__(self):
         # dos listas vacías, una por cada ejército
         vikingArmy = []
         saxonArmy = []
         #métodos (addViking, addSaxon, vikingAttack, saxonAttack, showStatus)
    def addViking(x):
         vikingArmy.append(x)
    def addSaxon(y):
         saxonArmy.append(y)
    def vikingAttack():
         Saxon.receiveDamage = Viking.strength
         return Viking.strength
    def saxonAttack():
         Viking.receiveDamage = Saxon.strength
         return Saxon.strength
    def showStatus():
         if saxonArmy == 0:
            return f"Vikings have won the war of the century!"
         elif vikingArmy == 0:
            return f"Saxons have fought for their lives and survive another day..."
         elif saxonArmy and vikingArmy >= 1:
            return f"Vikings and Saxons are still in the thick of battle."


