from queue import PriorityQueue
import time

from lab1.Tasks.data_loader import load_data


# Getting required parameters
def ucs_algo(G, Dist, Cost, start_node='1', end_node='50'):
    """
      Executes Uniform Cost Search Algorithm to find the optimal path between start and end nodes.

      :param dict G: The adjacency list representation of the graph where the keys are node IDs and the values are lists of neighboring node IDs.
      :param dict Dist: A dictionary with keys as string representations of edges (e.g., '1,2') and values as distances between the nodes.
      :param dict Cost: A dictionary with keys as string representations of edges (e.g., '1,2') and values as costs associated with traversing the edge.
      :param str start_node: Default is '1'.
      :param str end_node: Default is '50'.

      :return: A tuple containing the shortest distance, the total cost, and the optimal path as a list of node IDs.
      :rtype: tuple
      """
    priority_queue = PriorityQueue()
    priority_queue.put((0, 0, [start_node]))  # Distance, Cost, Path
    visited_nodes = set()
    visited_nodes.add(start_node)

    while not priority_queue.empty():
        current_distance, current_cost, current_path = priority_queue.get()
        current_node = current_path[-1]
        visited_nodes.add(current_node)

        if current_node == end_node:
            return current_distance, current_cost, current_path

        for neighbor in G[current_node]:
            if neighbor not in visited_nodes:
                new_path = current_path + [neighbor]
                edge_pair = ','.join([current_node, neighbor])
                new_distance = current_distance + Dist[edge_pair]
                new_cost = current_cost + Cost[edge_pair]
                priority_queue.put((new_distance, new_cost, new_path))


def run_ucs():
    try:
        start_time = time.time()
        G, Dist, Cost = load_data()
        ucs_results = ucs_algo(G, Dist, Cost)
        print("Time taken: %s seconds" % (time.time() - start_time))
        shortest_distance = ucs_results[0]
        total_cost = ucs_results[1]
        optimal_path = ucs_results[2]
        print("Shortest path: ", '->'.join(optimal_path))
        print("Shortest distance: ", shortest_distance)
        print("Total energy cost: ", total_cost)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

