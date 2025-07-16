# Lab 6 Gabriel Chun

import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        winner = random.choice([self, opponent])
        print(f'{winner.name} wins')

    def add_ability(self, ability):
        self.abilities.append(ability)
        print(f'{ability.name} has been added to {self.name}')

    def sum_of_attacks(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
        
    def add_armor(self, armor):
        self.armors.append(armor)
        print(f'{armor.name} has been added to {self.name}')

    def defend(self):
        blocked_damage = 0
        for armor in self.armors:
            blocked_damage += armor.block()
        return blocked_damage

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(f'Starting HP: {my_hero.current_health}')  # 200

    my_hero1 = Hero("Black Panther", 150)
    print(my_hero1.name)            
    print(f'Starting HP: {my_hero1.current_health}')  

    my_hero.battle(my_hero1)
    fireball = Ability('Fireball', 50)
    lightning = Ability('Lightning', 60)
    telekinesis = Ability('Telekinesis', 40)
    my_hero.add_ability(fireball)
    my_hero.add_ability(lightning)
    my_hero.add_ability(telekinesis)
    print(my_hero.sum_of_attacks())
    shield = Armor('Shield', 30)
    helmet = Armor('Helmet', 20)
    forcefield = Armor('Force Field', 60)
    my_hero.add_armor(shield)
    my_hero.add_armor(helmet)
    my_hero.add_armor(forcefield)
    print(my_hero.defend())