#!/usr/bin/env python
"""
Battle Simulator

Author: Mohammed Mohideen M Z
Date: June 11, 2025
Description: A Python module for battle simulator to identify efforts to win over opponents
"""


from platoon import *
import inspect
import platoon
import itertools
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class BattleSimulator:
    """Battle Simulator class is used to identify efforts required to compete and find the winning possibility"""

    def __init__(self, own, enemy):
        self.own_platoons = self.platoon_parser(own)
        self.enemy_platoons = self.platoon_parser(enemy)

    # self.advantages = {
    #     'Militia': [ 'Spearmen', 'LightCavalry' ]
    #      ...
    # }  # can use this object instead i have created separate class to main as like unit classes for each platoons

    @property
    def advantages(self) -> dict:
        """To Retrieve Platoons and their Advantages"""
        return { obj: getattr(platoon, obj).advantages
            for obj in platoon.__all__ 
            if inspect.isclass(getattr(platoon, obj))
        }
    
    @staticmethod
    def platoon_parser(obj: list) -> list:
        """To parse User input by splitting using special characters to retrieve platoons and its soldiers"""
        return [tuple(inp.split('#')) for inp in obj]

    def effort_advantage(self, own_platoons, e_platoon):
        """Method helps to retrieve effort count of own platoon against opponents when platoon has an advantages"""
        o_platoon, o_ct = own_platoons[0], int(own_platoons[1])
        if e_platoon in self.advantages[o_platoon]:
            return o_ct * 2
        return o_ct

    def battle_result(self) -> str:
        """ Method to Initiate permutation to identify best possible platoons to win over opponent """
        victory_ct = draw_ct = loss_ct = 0
        for _own_platoons in itertools.permutations(self.own_platoons):
            for ind, _own in enumerate(_own_platoons):
                _enemy_plt, _enemy_ct = self.enemy_platoons[ind]
                if _own[0] == _enemy_plt or _enemy_plt in self.advantages[_own[0]]:
                    own_ct = self.effort_advantage(_own, _enemy_plt)
                    if own_ct > int(_enemy_ct):
                        logger.info(f'Your {_own[0]} won over Enemies {_enemy_plt}!')
                        victory_ct += 1
                    elif own_ct == _enemy_ct:
                        draw_ct += 1
                        logger.info(f'Your {_own[0]} neither win nor lost aginst Enemies {_enemy_plt}!')
                    else:
                        loss_ct += 1
                        logger.info(f'Your {_own[0]} lost against Enemies {_enemy_plt}!')
                if victory_ct >= 3:
                    troop = ';'.join((f"{plt}#{ct}" for plt, ct in _own_platoons)) 
                    logger.info(f"Winning Arrangements (platoons): {troop}")
                    return troop
        if victory_ct < 3:
            logger.error('There is no Chance of Winning!')
            return "There is no Chance of Winning!"

def input_validator(inp, tot_attack=5):
    """Function used to validate user input"""
    query = inp.strip(';').split(';')
    if len(query) != tot_attack:
        logger.error("Platoons should be {tot_attack}! Please Retry with Valid Input!")
        exit()
    return query

def main():
    """Main function trigger this battle simulator"""
    tot_attack = 5 # to change please use this -> int(input("Enter total number of attack locations:"))
    own_platoon = input_validator(input("Enter your own Platoons:"), tot_attack)
    enemy_platoon = input_validator(input("Enter your opponent Platoons:"), tot_attack)
    battle = BattleSimulator(own_platoon, enemy_platoon)
    return f"Result: {battle.battle_result()}"


if __name__ == '__main__':
    print(main())
