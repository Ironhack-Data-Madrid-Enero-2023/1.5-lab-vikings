
# Soldier


class Soldier:
     def __init__(self, health, strength):
        self.health=health
        self.strength=strength

     def attack(self):
        return self.strength

     def receiveDamage(self, Damage):
        self.health -= Damage

            


# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength(Viking)

    def receiveDamage(self, Damage):
        if health<Damage:
            print(f'{self.name} has died in act of comba')

        

        else:
            health-=Damage
        print(f'{self.name}  has received {self.Damage} points of damage' )

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self, Damage):
        if health<Damage:
            print(f'A SAXON has died in act of comba')

        else:
            health-=Damage
        print(f'A SAXON has received {self.Damage} points of damage' )



    

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]


    def addViking(Viking):
        vikingArmy.append(Viking=+1)

    def addSaxon(Saxon):
        saxonArmy.append(Saxon=+1)

    def vikingAttack(self):
        if receiveDamage(Saxon)<strength(Viking):
            addSaxon-=1

        else:
            addSaxon==addSaxon

    def saxonAttack(self):
        if receiveDamage(Viking)<strength(Saxon):
            addViking-=1
        else:
            addViking==addViking


    def showStatus(self):
        if vikingArmy > saxonArmy:
            print( "Vikings have won the war of the century!")

        elif saxonArmy > vikingArmy:
            print("Saxons have fought for their lives and survive another day...")

        else:
            print("Vikings and Saxons are still in the thick of battle.")
