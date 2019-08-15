"""
By Jessica Angela Campisi
Date 8/15/2019
Just a sandbox for classes
"""
from random import randrange as rrange
from time import sleep as wait

class Player:
    def __init__(self, name, charClass, ai):
        self.name = name
        self.charClass = charClass
        self.enemy = Player
        self.ai = ai
        if self.charClass is 'mage':
            self.health = 60
            self.maxhealth = 60
            self.mana = 50
            self.maxmana = 50
            self.defense = 2
            self.attack = 2
        elif self.charClass is 'warrior':
            self.health = 100
            self.maxhealth = 100
            self.mana = 10
            self.maxmana = 10
            self.defense = 5
            self.attack = 5

    def setenemy(self, enemy):
        self.enemy = enemy

    def getname(self):
        return self.name

    def getclass(self):
        return self.charClass

    def gethealth(self):
        return self.health

    def getmana(self):
        return self.mana

    def getdefense(self):
        return self.defense

    def getattack(self):
        return self.attack

    # Prints off the player's stats.
    def printplayer(self):
        print('Player Name: {} \n'
              'Class: {}\n'
              'Health: {}\n'
              'Mana: {}\n'
              'Defense: {}\n'
              'Attack: {}\n'.format(self.getname(), self.getclass(), self.gethealth(), self.getmana(),
                                    self.getdefense(),
                                    self.getattack()))

    # Mage Functions ---------------------------------------------
    # casts a fireball. For now this does a base damage of 6 to 14. This is influenced by the player attack and
    # enemy defense.
    def castfireball(self):
        damage = rrange(6, 15) - self.enemy.getdefense() + self.getattack()
        self.enemy.health = self.enemy.health - damage
        print("{} has done {} damage to {} with a fireball! {} now has {} health remaining!".format(
            self.getname(), damage, self.enemy.getname(), self.enemy.getname(), self.enemy.gethealth()))

    def castheal(self):
        self.health += rrange(1, 20)

    # checks to see if the player has enough mana to cast the spell. Only returns true if yes. Else returns false
    # automatically
    def checkmana(self, cost):
        if self.mana >= cost:
            return True
        return False

    # Provides a list of choices for the excited mage to choose from. If they are low on mana or make a wrong choice
    # it will take that into consideration.
    def mageMenu(self):
        if self.ai:
            choice = rrange(1, 4)
        else:
            print("1. Cast Fireball (6 mana) "
                  "\n2. Cast Heal (4 mana)"
                  "\n3. Rest... (+4 mana)")
            choice = input("Selection: ")
        if choice:
            choice = int(choice)

        if choice is 1:
            if self.checkmana(6):
                self.castfireball()
                self.mana -= 6
            else:
                print("You are out of mana! Choose another option, I suggest resting...")
                self.mageMenu()
        elif choice is 2:
            if self.checkmana(4):
                if self.gethealth() >= self.maxhealth:
                    print("You're already at max health! Choose again!")
                    self.mageMenu()
                else:
                    self.castheal()
                    self.mana -= 4
            else:
                print("You are out of mana! Choose another option, I suggest resting...")
                self.mageMenu()
        elif choice is 3:
            if self.mana < self.maxmana:
                print("Resting.... ah... so nice... Probably going to get punched a lot. Just saying.")
                self.mana += 4
            else:
                print("Resting, but not going to recover anything... probably should have done something else... ")
        else:
            print("\nBad choice, try again..")

            self.mageMenu()
            if self.ai:
                choice = rrange(1, 4)
            else:
                print("1. Cast Fireball (6 mana) "
                      "\n2. Cast Heal (4 mana)"
                      "\n3. Rest... (+4 mana)")
                choice = input("Selection: ")
            if choice:
                choice = int(choice)

    # Warrior functions
    def warriorMenu(self):
        if self.ai:
            choice = rrange(1, 4)
        else:
            print("1. Attack with Sword (No Mana) "
                  "\n2. Power Attack (3 mana)"
                  "\n3. Rest... (+2 mana)")
            choice = input("Selection: ")
        if choice:
            choice = int(choice)
        if choice is 1:

    def swordattack(self):
        damage = rrange(1, 9)
        self.enemy.health -= damage - self.enemy.defense + self.attack




player = Player('Bob', 'mage', False)
computer = Player('Malfoy', 'warrior', True)
player.setenemy(computer)

player.printplayer()
print("\n")


while computer.gethealth() > 0:
    player.printplayer()
    player.mageMenu()
    wait(1.5)

print("{} has defeated {} with a flurry of fireballs!".format(player.getname(), computer.getname()))