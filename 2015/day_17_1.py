'''
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
'''

import req
import utils

CONTAINER_COMB = []
EGGNOG = 150
GLOBAL_DATA = {}

def checkandaddcomb(containers):
    global CONTAINER_COMB
    for container in CONTAINER_COMB:
        if(len(container) != len(containers)):
            continue
        
        if(sorted(container) == sorted(containers)):
            return
        
    CONTAINER_COMB.append(containers[:])

def rec(usedContainers, unUsedContainers, remEggnog):
    if(remEggnog < 0):
        return
    
    if(remEggnog == 0):
        checkandaddcomb(usedContainers)
        return
    
    for i in range(len(unUsedContainers)):
        cId = unUsedContainers.pop(i)
        usedContainers.append(cId)
        rec(usedContainers,unUsedContainers,remEggnog - GLOBAL_DATA[cId])
        usedContainers.pop(-1)
        unUsedContainers.insert(i,cId)

def main():
    input_data = utils.getInputLines(2015,17)
    
    index = 0
    for data in input_data:
        GLOBAL_DATA[index] = int(data)
        index += 1

    usedContainers = []
    unUsedContainers = [x for x,_ in GLOBAL_DATA.items()]
    rec(usedContainers,unUsedContainers,EGGNOG)

    print(len(CONTAINER_COMB))
if __name__ == '__main__':
    main()