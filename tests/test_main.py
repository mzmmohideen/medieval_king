"""
Battle Simulator Test Cases

Author: Mohammed Mohideen M Z
Date: June 11, 2025
Description: Simple Unitest case used to test BattleSimulator Response
"""

import unittest
from main import BattleSimulator, input_validator

class TestBattleSimulator(unittest.TestCase):

    def test_min_winning_possibility(self):
        own_platoon = input_validator("Spearmen#10;Militia#30;FootArcher#20;LightCavalry#1000;HeavyCavalry#10")
        enemy_platoon = input_validator("Militia#10;Spearmen#10;FootArcher#1000;LightCavalry#120;CavalryArcher#100")
        battle = BattleSimulator(own_platoon, enemy_platoon)
        result = battle.battle_result()
        self.assertEqual(len(input_validator(result)), 5)
