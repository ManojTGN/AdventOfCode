'''
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
'''

import req
import utils

MAX_MATCH = 0
GLOBAL_DATA = {}

def main():
    global MAX_MATCH
    input_data = utils.getInputLines(2015,16)
    ticker_tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    
    for data in input_data:
        sdata = data.split(' ',2)
        name = ' '.join(sdata[:2])[:-1]
        GLOBAL_DATA[name] = {'data':{}}
        rdata = sdata[-1].split(', ')
        for d in rdata:
            spd = d.split(': ')
            GLOBAL_DATA[name]['data'][spd[0]] = int(spd[-1])
    
    NAME = ''
    for name,data in GLOBAL_DATA.items():
        match = 0
        for item_name,item_data in data['data'].items():
            if(item_name in ticker_tape and item_data == ticker_tape[item_name]):
                match+=1
        if(match > MAX_MATCH):
            MAX_MATCH = match
            NAME = name
    
    print(NAME.split(' ')[-1])


if __name__ == '__main__':
    main()