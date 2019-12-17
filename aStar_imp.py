from pathfinding import *

start_goal , end_goal = (0, 0) , (5, 5)

class node:
    def __init__(self):
        self.upNode = None
        self.downNode = None
        self.leftNode = None
        self.rightNode = None

    def flood_fill(self, loc, map, graph):
        if loc[1] > 0 and graph[loc[1]-1][loc[2]] != None:
            pass
        #and other four directions are not equal to None
        #return

        #recursive
        if loc[1] > 0 and graph[loc[1] - 1][loc[2]] == None and map[loc[1]]:
            graph[loc[1]-1][loc[2]] = newNode = node()

            newNode.Right=graph[loc[1]loc[2]]
            graph[loc[1]][loc[2]].left = newNode
            floodfill((loc[1]-1, loc[2]))

        pass