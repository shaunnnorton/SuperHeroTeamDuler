from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")
    
    def create_ability(self):
        name = input("What is the ability name?   ")
        max_damage = int(input("What is the max damage of the ability?   "))
        return Ability(name,max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?  ")
        max_damage = int(input("What si the max damage of the weapon?   "))
        return Weapon(name,max_damage)

    def create_armor(self):
        name = input("What is the name of your armor?   ")
        max_block = int(input("What is the max blocking power of your armor?   "))
        return Armor(name,max_block)

    def create_hero(self):
        '''Prompt user for Hero information return Hero with values from user input.'''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #TODO add an ability to the hero
               hero.add_ability(self.create_ability())
           elif add_item == "2":
               #TODO add a weapon to the hero
               hero.add_weapon(self.create_weapon())
           elif add_item == "3":
               #TODO add an armor to the hero
               hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            print(f"Hero {i} created")


    def build_team_two(self):
        
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            print(f"Hero {i} created")


    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"{self.team_two.name} average K/D was: {team_kills/team_deaths}")

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(f"survived from {self.team_two.name}: {hero.name}")
#yay im done
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
