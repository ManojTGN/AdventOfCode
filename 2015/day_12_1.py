'''
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
'''

import req
import json
import utils

GLOBAL_SUM = 0

def walk(data):
    global GLOBAL_SUM
    if isinstance(data, dict):
        for _, value in data.items():
            walk(value)
    elif isinstance(data, list):
        for i in data:
            walk(i)
    elif isinstance(data, int):
        GLOBAL_SUM += data

def main():
    input_data = utils.getInputLines(2015,12)

    for data in input_data:
        walk(json.loads(data))
    
    print(GLOBAL_SUM)

if __name__ == '__main__':
    main()