import random
class Ninja:
    def __init__(self, ninjatype, username, health=100, specialmove=0, attacktype=""):
        self.ninjatype = ninjatype
        self.username= username
        self.health = health
        self.specialmove= specialmove
        self.attacktype=attacktype

    def decreaseHealth(self, health):
        self.health-=health
        return self

    def attack(self,other_ninja,attacktype):
            if attacktype=="Sword":
                health=20
            else:
                health=10*round(random.random()*3)
            other_ninja.decreaseHealth(health)
            return self
    def display_ninja_stats(self):
        print("Username is", self.username)
        print("Health is", self.health)
        return self



username = input("PlayerOne:")
ninjatype = input("Pick Hanzo or Miriku?:")
ninja1 = Ninja(ninjatype, username, specialmove=10)
username2 = input("PlayerTwo:")
ninjatype2 = input("Pick Hanzo or Miriku?:")
ninja2 = Ninja(ninjatype2, username2, specialmove=10)
while ninja1.health>0 and ninja2.health>0:
    attacktype=input("Attack Player Two with Sword or Ninja Star?")
    ninja1.attack(ninja2,attacktype)
    ninja1.display_ninja_stats()
    ninja2.display_ninja_stats()
    if ninja2.health==0:
        print("Player 1 Wins")
        break
    attacktype=input("Attack Player One with Sword or Ninja Star?")
    ninja2.attack(ninja1,attacktype)
    ninja2.display_ninja_stats()
    ninja1.display_ninja_stats()
    if ninja1.health==0:
        print("Player 2 Wins")
        break
