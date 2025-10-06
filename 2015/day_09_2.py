'''
  --- Day 9: All in a Single Night ---
  Every year, Santa manages to deliver all of his presents in a single night.
  
  This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?
  
  For example, given the following distances:
  
  London to Dublin = 464
  London to Belfast = 518
  Dublin to Belfast = 141
  The possible routes are therefore:
  
  Dublin -> London -> Belfast = 982
  London -> Dublin -> Belfast = 605
  London -> Belfast -> Dublin = 659
  Dublin -> Belfast -> London = 659
  Belfast -> Dublin -> London = 605
  Belfast -> London -> Dublin = 982
  The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
  
  What is the distance of the shortest route?
  --- Part Two ---
  The next year, just to show off, Santa decides to take the route with the longest distance instead.
  He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.
  
  For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
  What is the distance of the longest route?

'''

import req
import utils

GLOBAL_DATA = {}
MAX_DISTANCE = float('-inf')

def rec(node, dist, visited_node):
    global GLOBAL_DATA,MAX_DISTANCE
    if(len(GLOBAL_DATA) == len(visited_node)):
        if(dist > MAX_DISTANCE):
            MAX_DISTANCE = dist
        return True
    
    node_data = None
    if(node in GLOBAL_DATA):
        node_data =  GLOBAL_DATA[node]

    if(node_data):
        for index,_node in enumerate(node_data['nodes']):
            if(_node not in visited_node):
                visited_node.append(_node)
                rec(_node,dist + node_data['distance'][index],visited_node)
                visited_node.remove(_node)

    return False

def main():
    input_data = utils.getInputLines(2015,9)
    
    for data in input_data:
        sData = data.split(' ')
        _from = sData[0]
        _to = sData[2]
        _dist = sData[-1]

        if _from in GLOBAL_DATA:
            GLOBAL_DATA[_from]['nodes'].append(_to)
            GLOBAL_DATA[_from]['distance'].append(int(_dist))
        else:
            GLOBAL_DATA[_from] = {'nodes':[_to],'distance':[int(_dist)]}
    
        if _to in GLOBAL_DATA:
            GLOBAL_DATA[_to]['nodes'].append(_from)
            GLOBAL_DATA[_to]['distance'].append(int(_dist))
        else:
            GLOBAL_DATA[_to] = {'nodes':[_from],'distance':[int(_dist)]}

    for node in GLOBAL_DATA:
        rec(node, 0, [node])
    
    print(MAX_DISTANCE)
if __name__ == '__main__':
    main()