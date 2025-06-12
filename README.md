# 🛡️ Battle Simulator

**Author:** Mohammed Mohideen M Z  
**Date:** June 11, 2025  
**Language:** Python 3.9+  
**Description:** A Python-based battle simulator to determine the battle arrangement to win over opponents platoons.

---

## Problem Statement

You are a medieval king attacking your opponent at five locations simultaneously
Each location has a platoon - which has a number of soldiers of a specific class
You know the platoons your opponent has
Your job is to figure out which of your platoons should attack which of your opponent's platoons so that you can win majority of the battles.
Your goal is to:

> **Win at least 3 out of 5 battles** based on platoon strengths and class advantages.

There are 6 classes of soldiers:

- Militia
- Spearmen
- Light Cavalry
- Heavy Cavalry
- Foot Archer
- Cavalry Archer

---

## How to run?

```python main.py```

## Result:

```
$ python main.py 
Enter your own Platoons:Spearmen#10;Militia#30;FootArcher#20;LightCavalry#1000;HeavyCavalry#10
Enter your opponent Platoons:Militia#10;Spearmen#10;FootArcher#1000;LightCavalry#120;CavalryArcher#100
2025-06-12 12:00:07,828 - INFO - Your Militia won over Enemies Spearmen!
2025-06-12 12:00:07,828 - INFO - Your FootArcher lost against Enemies FootArcher!
2025-06-12 12:00:07,828 - INFO - Your LightCavalry won over Enemies LightCavalry!
2025-06-12 12:00:07,828 - INFO - Your Militia won over Enemies Spearmen!
2025-06-12 12:00:07,828 - INFO - Winning Arrangements (platoons): Spearmen#10;Militia#30;FootArcher#20;HeavyCavalry#10;LightCavalry#1000
Result: Spearmen#10;Militia#30;FootArcher#20;HeavyCavalry#10;LightCavalry#1000
```

## Sample Test Result
```
$ python -m unittest tests/test_main.py 
2025-06-12 12:00:34,548 - INFO - Your Militia won over Enemies Spearmen!
2025-06-12 12:00:34,548 - INFO - Your FootArcher lost against Enemies FootArcher!
2025-06-12 12:00:34,548 - INFO - Your LightCavalry won over Enemies LightCavalry!
2025-06-12 12:00:34,548 - INFO - Your Militia won over Enemies Spearmen!
2025-06-12 12:00:34,548 - INFO - Winning Arrangements (platoons): Spearmen#10;Militia#30;FootArcher#20;HeavyCavalry#10;LightCavalry#1000
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
