# By Jessica Angela Campisi
# 4/1/2018
# Randomly choose what character race & class that is played

# Imports
import random, sys
random.seed()

# Alliance or Horde
faction = ["Horde", "Alliance"]

# Alliance Races
allianceRaces = ["Human", "Night Elf", "Gnome", "Dwarf", "Worgen", "Draenei", "Panda"]

# Horde Races
hordeRaces = ["Orc", "Troll", "Undead", "Tauren", "Goblin", "Blood Elf", "Panda"]

# Race / Classes
humanClasses = ["Warrior", "Rogue", "Hunter", "Monk", "Mage", "Priest", "Warlock", "Paladin", "Death Knight"]
nelfClasses = ["Warrior", "Rogue", "Hunter", "Monk", "Mage", "Priest", "Druid", "Death Knight"]
gnomeClasses = ["Warrior", "Rogue", "Monk", "Priest", "Mage", "Warlock", "Hunter", "Death Knight"]
dwarfClasses = ["Warrior", "Rogue", "Monk", "Priest", "Mage", "Warlock", "Hunter", "Paladin", "Shaman", "Death Knight"]
worgenClasses = ["Warrior", "Rogue", "Priest", "Mage", "Warlock", "Hunter", "Druid", "Death Knight"]
draeneiClasses = ["Warrior", "Rogue", "Priest", "Monk", "Mage", "Paladin", "Hunter", "Shaman", "Death Knight"]
pandaClasses = ["Warrior", "Rogue", "Monk", "Priest", "Mage", "Shaman", "Hunter"]
orcClasses = ["Warrior", "Rogue", "Hunter", "Monk", "Mage", "Priest", "Warlock", "Paladin", "Death Knight"]
trollClasses = ["Warrior", "Rogue", "Hunter", "Monk", "Mage", "Priest", "Druid", "Death Knight"]
taurenClasses = ["Warrior", "Paladin", "Monk", "Priest", "Mage", "Shaman", "Hunter", "Death Knight"]
goblinClasses = ["Warrior", "Rogue", "Monk", "Priest", "Mage", "Warlock", "Hunter", "Paladin", "Shaman", "Death Knight"]
undeadClasses = ["Warrior", "Rogue", "Priest", "Mage", "Warlock", "Hunter", "Monk", "Death Knight"]
belfClasses = ["Warrior", "Rogue", "Monk", "Priest", "Mage", "Warlock", "Hunter", "Paladin", "Death Knight"]

factionChoice = random.choice(faction)

# Race Choice
if factionChoice is "Horde":
    raceChoice = random.choice(hordeRaces)
else:
    raceChoice = random.choice(allianceRaces)
# Class choice
if raceChoice is "Human":
    classChoice = random.choice(humanClasses)
elif raceChoice is "Gnome":
    classChoice = random.choice(gnomeClasses)
elif raceChoice is "Dwarf":
    classChoice = random.choice(dwarfClasses)
elif raceChoice is "Worgen":
    classChoice = random.choice(worgenClasses)
elif raceChoice is "Draenei":
    classChoice = random.choice(worgenClasses)
elif raceChoice is "Panda":
    classChoice = random.choice(pandaClasses)
elif raceChoice is "Orc":
    classChoice = random.choice(orcClasses)
elif raceChoice is "Troll":
    classChoice = random.choice(trollClasses)
elif raceChoice is "Goblin":
    classChoice = random.choice(goblinClasses)
elif raceChoice is "Undead":
    classChoice = random.choice(undeadClasses)
elif raceChoice is "Tauren":
    classChoice = random.choice(taurenClasses)
elif raceChoice is "Blood Elf":
    classChoice = random.choice(belfClasses)


# display results
print("Faction: {}".format(factionChoice))
print("Race: {}".format(raceChoice))
print("Class: {}".format(classChoice))

