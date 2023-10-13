import time
from queue import PriorityQueue
from Tasks.data_loader import load_data

# Constant Weights decided through trial and error
COST_WEIGHT = 0.1
DIST_WEIGHT = 0.9

def ucs_refined_algorithm(G, Dist, Cost, energy_budget, start_node='1', end_node='50'):
    """
    Execute Uniform Cost Search Algorithm with dynamic weights, considering energy constraints, to find the optimal path.

    Args:
        G (dict): The graph as an adjacency list.
        Dist (dict): A dictionary with distances between nodes.
        Cost (dict): A dictionary with costs associated with edges.
        energy_budget (float): The maximum allowed energy budget.
        start_node (str): The starting node.
        end_node (str): The ending node.

    Returns:
        tuple: A tuple containing the shortest distance, total cost, and optimal path.
    
    """
    pq = PriorityQueue()
    pq.put((0, 0, 0, start_node))  # WeightedDistCost, Dist, Cost, Node
    explored_nodes = {start_node: 0}
    parent_nodes = {start_node: None}

    while not pq.empty():
        weighted_dist_cost, dist, cost, current_node = pq.get()

        if current_node == end_node:
            path = [current_node]
            while parent_nodes[current_node] is not None:
                path.append(parent_nodes[current_node])
                current_node = parent_nodes[current_node]

            return dist, cost, path[::-1]

        for neighbor in G[current_node]:
            edge_pair = ','.join([current_node, neighbor])
            new_dist = dist + Dist[edge_pair]
            new_cost = cost + Cost[edge_pair]
            
            remaining_budget = energy_budget - new_cost
            # Check if there is enough budget to explore this neighbor
            if remaining_budget >= 0:
                # Calculate the weight to balance cost and distance
                # Weights are applied to balance the trade-off between minimizing energy cost
                # and minimizing distance, to ensure an optimal path while considering energy constraints.
                cost_weight = min(COST_WEIGHT, remaining_budget / (new_dist + 1e-6))
                dist_weight = 1 - cost_weight
                
                # Apply weights to cost and distance
                weighted_cost = new_cost * cost_weight
                weighted_dist = new_dist * dist_weight

                # Combine the weighted cost and distance to form the new weighted distance cost
                new_weighted_dist_cost = weighted_cost + weighted_dist

                # Check if this neighbor node has not been explored or if the new path is better
                if neighbor not in explored_nodes or new_weighted_dist_cost < explored_nodes[neighbor]:
                    explored_nodes[neighbor] = new_weighted_dist_cost
                    parent_nodes[neighbor] = current_node
                    pq.put((new_weighted_dist_cost, new_dist, new_cost, neighbor))

def run_ucs_refined(energy_budget):
    try:
        start_time = time.time()
        G, Dist, Cost = load_data()
        ucs_results = ucs_refined_algorithm(G, Dist, Cost, energy_budget)
        print("Time taken: %s seconds" % (time.time() - start_time))
        shortest_distance = ucs_results[0]
        total_cost = ucs_results[1]
        optimal_path = ucs_results[2]
        print("Shortest path: ", '->'.join(map(str, optimal_path)))
        print("Shortest distance: ", shortest_distance)
        print("Total energy cost: ", total_cost)
        print("Energy budget: ", energy_budget)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
