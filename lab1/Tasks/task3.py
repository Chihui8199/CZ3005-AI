from .data_loader import load_data
import time
from queue import PriorityQueue
import math
import heapq

G, Dist, Cost, Coord = load_data()

#http://www.cs.cornell.edu/courses/cs312/2007sp/recitations/rec26.html#:~:text=An%20obvious%20choice%20for%20a,current%20node%20and%20the%20destination.

import numpy as np
import heapq


    
def euclidean(Coord, source, destination):
    x1, y1 = Coord[source]
    x2, y2 = Coord[destination]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def write_output(path, finalDist, finalEnergy):
    pathString = '->'.join(path)
    formattedPathString = '\n'.join(pathString[i:i + 64] for i in range(0, len(pathString), 64))
    print('Shortest path:')
    print('\n')
    print(formattedPathString)
    print('\n')
    print('Shortest distance: ' + str(finalDist))
    print('\n')
    print('Total energy cost: ' + str(finalEnergy))

def run_astar(source='1', destination='50', weight=1.05):
    energyBudget = 287932
    w = weight
    aStarCost = aStarValue = w
    heap = [(aStarCost, 0, 0, source, [source])]

    costToNode = {source: 0}
    distToNode = {source: 0}
    aStarNode = {source: aStarValue}

    finalDist = 0
    finalEnergy = 0
    path = []

    found = False

    while heap:
        aStarCost, currPathCost, currEnergyCost, currNode, prevPath = heapq.heappop(heap)
        #print(currNode)
        #print(G["1"])
        #break

        if currNode == destination:
            path = prevPath
            finalEnergy = currEnergyCost
            finalDist = currPathCost
            found = True
            break

        for neighbor in G[currNode]:
            nextEnergyCost = Cost[currNode + ',' + neighbor]
            if nextEnergyCost + currEnergyCost > energyBudget:
                continue
            nextPathCost = Dist[currNode + ',' + neighbor]
            nextAStarCost = nextPathCost + w * euclidean(Coord, neighbor, destination)
            temp = (nextAStarCost, currPathCost + nextPathCost, currEnergyCost + nextEnergyCost, neighbor, prevPath + [neighbor])
            if temp[0] < aStarNode.get(neighbor, float('inf')) or temp[2] < costToNode.get(neighbor, float('inf')):
                aStarNode[neighbor] = temp[0]
                distToNode[neighbor] = temp[1]
                costToNode[neighbor] = temp[2]
                heapq.heappush(heap, temp)

    if not found:
        print('Path not found')
        return

    write_output(path, str(finalDist), str(finalEnergy))
    
    
