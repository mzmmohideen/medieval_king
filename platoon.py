"""
Battle Simulator

Author: Mohammed Mohideen M Z
Date: June 11, 2025
Description: A Python module used to define platoons and their advantages
"""

__all__ = ['Militia', 'Spearmen', 'LightCavalry', 'HeavyCavalry', 'CavalryArcher', 'FootArcher']


class Militia:
    advantages = [ 'Spearmen', 'LightCavalry' ]


class Spearmen:
    advantages = [ 'LightCavalry', 'HeavyCavalry' ]


class LightCavalry:
    advantages = [ 'FootArcher', 'CavalryArcher' ]


class HeavyCavalry:
    advantages = [ 'Militia', 'FootArcher', 'LightCavalry' ]


class CavalryArcher:
    advantages = [ 'Spearmen', 'HeavyCavalry' ]


class FootArcher:
    advantages = [ 'Militia', 'CavalryArcher' ]
