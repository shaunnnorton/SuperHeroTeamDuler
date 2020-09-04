import random
from ability import Ability
from armor import Armor
from weapon import Weapon
class Hero:
    def __init__(self,name,starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def fight(self,opponent):
        if len(opponent.abilities) == 0 and len(self.abilities) == 0:
            print("Its a draw!!")
            return
        else: 
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                print(f"{opponent.name} is at {opponent.current_health} health.")
                print(f"{self.name} is at {self.current_health} health.")
            if self.is_alive() == True:
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} has won!")
                return self
            else:
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{opponent.name} has won!")
                return opponent

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


    def add_ability(self,new_ability):
        self.abilities.append(new_ability)

    def attack(self):
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def is_alive(self):
        if self.current_health <= 0:
            return False
        return True

    
    def add_armor(self,new_armor):
        self.armors.append(new_armor)

    
    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self,damage):
        self.current_health -= (damage - self.defend(damage))

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())