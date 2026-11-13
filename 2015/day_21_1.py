'''
--- Day 21: RPG Simulator 20XX ---
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

'''

import req
import math
import utils

WEAPONS = {
    'Dagger'     :  {'cost': 8,     'damage':4,       'armor':0},
    'Shortsword' :  {'cost':10,     'damage':5,       'armor':0},
    'Warhammer'  :  {'cost':25,     'damage':6,       'armor':0},
    'Longsword'  :  {'cost':40,     'damage':7,       'armor':0},
    'Greataxe'   :  {'cost':74,     'damage':8,       'armor':0}
}

ARMORS = {
    'None'      :  {'cost': 0,     'damage':0,      'armor': 0},
    'Leather'    : {'cost':13,     'damage':0,      'armor': 1},
    'Chainmail'  : {'cost':31,     'damage':0,      'armor': 2},
    'Splintmail' : {'cost':53,     'damage':0,      'armor': 3},
    'Bandedmail' : {'cost':75,     'damage':0,      'armor': 4},
    'Platemail'  : {'cost':102,    'damage':0,      'armor': 5}
}

RINGS = {
    'None'      :  {'cost':   0,     'damage':0,      'armor': 0},
    'Damage +1' :  {'cost':  25,     'damage':1,      'armor': 0},
    'Damage +2' :  {'cost':  50,     'damage':2,      'armor': 0},
    'Damage +3' :  {'cost': 100,     'damage':3,      'armor': 0},
    'Defense +1':  {'cost':  20,     'damage':0,      'armor': 1},
    'Defense +2':  {'cost':  40,     'damage':0,      'armor': 2},
    'Defense +3':  {'cost':  80,     'damage':0,      'armor': 3}
}

VILLAN = {
    'hit_points': 0,
    'damage': 0,
    'armor': 0
}

YOU = {
    'hit_points': 100,
    'damage': 0,
    'armor': 0,
    'cost': 0
}

MIN_GOLD = math.inf

def play(weapon, armor, ring_1, ring_2):
    global MIN_GOLD
    YOU['hit_points'] = 100
    YOU['cost'] = 0
    YOU['damage'] = 0
    YOU['armor'] = 0
    
    for data in [WEAPONS[weapon], ARMORS[armor], RINGS[ring_1], RINGS[ring_2]]:
        YOU['cost'] += data['cost']
        YOU['damage'] += data['damage']
        YOU['armor'] += data['armor']

    turn = True
    TURN = [VILLAN.copy(), YOU]
    while( TURN[int(turn)]['hit_points'] > 0):
        damage = TURN[int(turn)]['damage']
        oppo_armor = TURN[int(not turn)]['armor']

        actual_damage = max(1, damage - oppo_armor)

        TURN[int(not turn)]['hit_points'] -= actual_damage

        turn = not turn

    if(not turn and YOU['cost'] < MIN_GOLD):
        MIN_GOLD = YOU['cost']

def main():
    input_data = utils.getInputLines(2015,21)

    for line in input_data:
        data = line.split(': ')
        VILLAN[data[0].replace(' ','_').lower()] = int(data[1])

    for weapon in WEAPONS:
        for armor in ARMORS:
            for ring_1 in RINGS:
                for ring_2 in RINGS:
                    play(weapon, armor, ring_1, 'None' if ring_2 == ring_1 else ring_2)

    print(MIN_GOLD)

if __name__ == '__main__':
    main()