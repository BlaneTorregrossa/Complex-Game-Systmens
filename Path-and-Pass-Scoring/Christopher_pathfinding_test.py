import math
import sys

class Node(object):
    '''data'''

    def __init__(self, guid, position):
        
        self.guid = ''
        if guid < 10:
            self.guid = str('0' + str(guid))
        else:
            self.guid = str(guid)

        self.pos = position
        self.h = 0
        self.g = 0
        self.f = self.h + self.g
        self.walkable = True
        self.neighbors = []
        self.parent = None

    def __getitem__(self, key):
        return self.pos[key]

    def __str__(self):
        '''str'''
        return str.format('({0}) ', self.guid)

def manhattan(start, goal):
    
    ydif = abs(goal[1] - start[1])
    xdif = abs(goal[0] - start[0])

    return xdif + ydif

    
def costtomove(start, goal):
    '''ctm'''
    if start[0] == goal[0] or start[1] == goal[1]:
        return 10
    return 14

def getneighbors(node, nodes):
    '''asdf'''
    current = node
    right = (current[0] + 1, current[1])
    top_right = (current[0] + 1, current[1] + 1)
    top = (current[0], current[1] + 1)
    top_left = (current[0] - 1, current[1] + 1)
    left = (current[0] - 1, current[1])
    bottom_left = (current[0] - 1, current[1] - 1)
    bottom = (current[0], current[1] - 1)
    bottom_right = (current[0] + 1, current[1] - 1)
    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:
        node = (i[0], i[1])
        if node in directions:
            neighbors.append(i)
    return neighbors

def retrace(goal):
    '''retrace'''
    current = goal
    path = []
    while current:
        path.append(current)
        current = current.parent
    return path
    
#   Fix ***
def christopher_astar(start, goal, graph):
    path = []
    openlist = []
    closedlist = []
    current = start

#   *** Everything below in this method

    if len(closedlist) <= 0:
        closedlist.append(start)
    while len(openlist) > 0:
        closedlist.append(current)
        openlist.remove(current)
        for node in getneighbors(current, graph):
            if node not in openlist and node not in closedlist:
                openlist.append(node)
            node.g = current.g + costtomove(current, node)
            tentative_g = node.g
            if node not in closedlist:
                pass
            if node in closedlist:
                pass
            node.h = manhattan(node, goal)
            node.f = node.g + node.h

        current = openlist[0]
        for node in range(0, len(openlist)):
            for nodecmp in range(0, len(openlist)):
                if openlist[nodecmp].f < openlist[node].f:
                    temp = openlist[nodecmp]
                    openlist[nodecmp] = openlist[node]
                    openlist[node] = temp

    path = closedlist
    return path

christopher_graph = []
COUNT = 0
for ypos in range(10):
    for xpos in range(10):
        christopher_graph.append(Node(COUNT, (xpos, ypos)))
        COUNT += 1

#   Bad ***
def main():
    '''main'''
    copygraph = list(christopher_graph)
    test = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]
    expected = []
    for i in test[3]:
        expected.append(copygraph[i])

    for i in unwalkable:
        copygraph[i].walkable = False

    #   Gives useless result
    result = christopher_astar(start, goal, copygraph)

    expectedres = []
    for i in expected:
        expectedres.append(int(i.guid))
    print str.format('start::{0} goal::{1} unwalkables::{2}', start, goal, unwalkable)

    actualres = []
    for i in result:
        actualres.append(int(i.guid))
    print str.format('expected result {0} \nactual   result {1}', expectedres, actualres)

if __name__ == '__main__':
    main()
