from .data_loader import load_data
import time
from queue import PriorityQueue
import math
import heapq

G, Dist, Cost, Coord = load_data()

#http://www.cs.cornell.edu/courses/cs312/2007sp/recitations/rec26.html#:~:text=An%20obvious%20choice%20for%20a,current%20node%20and%20the%20destination.

import numpy as np
import heapq
from math import sqrt


def heuristic(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def a_star(G,root, goal,max_energy):

    # create a priority queue of paths
    queue = PriorityQueue()
    queue.put((0, 0, 0,[root]))
    visited = set()
    visited.add(root)
    # iterate over the items in the queue
    while not queue.empty():
        # get the highest priority item
        pair = queue.get()
        current = pair[3][-1]
        visited.add(current)
        if current == goal:
            return pair
        # add all the edges to the priority queue
        for edge in G[current]:
            if edge not in visited:
                # create a new path with the node from the edge
                new_path = list(pair[3])
                new_path.append(edge)
                heuristic_func = heuristic(Coord[edge], Coord[goal])
                edge_pair = ','.join([current,edge])

                if (pair[2]+Cost[edge_pair])<=max_energy:
                    queue.put((0.9*pair[1]+Dist[edge_pair]+0.1*heuristic_func, pair[1] + Dist[edge_pair], pair[2]+Cost[edge_pair],new_path))

                else:
                    pass
    
    print("There is no path that the energy used is less than", max_energy)

def run_astar(energy_budget):
    start = time.time()
    result = a_star(G,'1', '50',energy_budget)
    print("Time taken: %s seconds" % (time.time() - start))
    Shortest_path = result[3]
    cost = result[2]
    Shortest_distance = result[1]

    path = ''
    for i in Shortest_path:
        path = path + '->' + i
    path = path[2:]

    print("Shortest path: ", path)
    print("Shortest distance: ", Shortest_distance)
    print("Total energy cost: ", cost)

