'''
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

Answer: 

'''

import req
import utils

def countTotallight(data):
    _count = 0
    for line in data:
        for light in line:
            if(light == '#'):
                _count += 1
    return _count

def count(data, x, y):
    _count = 0
    for _y in range(-1,2):
        for _x in range(-1,2):
            if(
                (_y == 0 and _x == 0) or
                (y + _y < 0 or y + _y > len(data)-1) or
                (x + _x < 0 or x + _x > len(data[0])-1)
               ):
                continue

            if(data[y + _y][x + _x] == '#'):
                _count+=1
    
    return _count

def gameoflife(data):
    newGol = [['.' for x in range(len(data[0]))] for y in range(len(data))]

    for y,line in enumerate(data):
        for x,light in enumerate(line):
            _count = count(data, x, y)
            if(_count != 2 and _count != 3):
                newGol[y][x] = '.'
            elif(_count == 3):
                newGol[y][x] = '#'
            else:
                newGol[y][x] = light

    newGol[0][0] = newGol[0][-1] = newGol[-1][0] = newGol[-1][-1] ='#'

    return newGol

def main():
    input_data = utils.getInputLines(2015,18)

    gol = []
    for data in input_data:
        gol.append(list(data))

    gol[0][0] = gol[0][-1] = gol[-1][0] = gol[-1][-1] ='#'

    for _ in range(100):
        gol=gameoflife(gol)

    print(countTotallight(gol))

if __name__ == '__main__':
    main()