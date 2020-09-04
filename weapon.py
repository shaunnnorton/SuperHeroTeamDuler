from ability import Ability
import random
class Weapon(Ability):
  def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # Pick a random value between 0 and self.max_damage
      random_value = random.randint(self.max_damage//2,self.max_damage)
      return random_value
