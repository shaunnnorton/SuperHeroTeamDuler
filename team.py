import random
class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        i = []
        for hero in self.heroes:
            i.append(hero.name)
        print(i)

    def add_hero(self,hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            l_hero=random.choice(living_heroes)
            l_oppo=random.choice(living_opponents)
            outcome = l_hero.fight(l_oppo)
            if outcome == l_oppo:
                living_heroes.remove(l_hero)
            else:
                living_opponents.remove(l_oppo)