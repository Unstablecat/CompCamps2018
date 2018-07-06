import random
import sys

name = input("who dares to challege MITs?")
Health = 40
score = 0

class MIT:
    """MITs - The Enemies"""
    def __init__ (self, name):
        self.name = name
        self.health = 30

    @property
    def damage(self):
        return random.randint(1,7)

    def isAlive(self):
        return self.health > 0


    def attack(self):
        damage = random.randint(0,10)
        self.health -= damage
        return damage
mits = [
    MIT("Kaitlen"),
    MIT("Travis"),
    MIT("Rhiannon"),
    MIT("Austin"),
    MIT("Bennett"),
]

random.shuffle(mits)

while len(mits) > 0:
    mit = mits.pop()
    print("a wild {} appears!".format(mit.name))
    while mit.isAlive():
        print("you have {} health.".format(Health))
        print("do you want to fight or flee")
        if input("fight / Flee > ").lower() == "fight":
            damage = mit.attack()
            score += damage

            print("you did {} damage".format(damage))
            if mit.isAlive():
                damage = mit.damage
                Health -= damage
                print("you took {} damage".format(damage))
        else:
            Caught = random.randint(1,5)==1
            if not Caught:
                print("you have escaped")
                print("your score was {}".format(score))
                sys.exit(0)
            else:
                print("you failed to flee")
print("WOW! you have done it!")
print("Good work{}!".format(name))
print("the MITs have been removed from comp camp")
print("your score is {}".format(score))
