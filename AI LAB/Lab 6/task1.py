import heapq


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 5), ('E', 12)],
    'C': [('A', 3), ('E', 7)],
    'D': [('B', 5)],
    'E': [('C', 7), ('B', 12)]
}

def uniform_cost_search(graph, start, goal):
    
    queue = []
    heapq.heappush(queue, (0, start, [start])) 

    visited = set()

    while queue:
        cost, current_node, path = heapq.heappop(queue)

        if current_node in visited:
            continue

        if current_node == goal:
            return cost, path

        visited.add(current_node)

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in visited:
                total_cost = cost + edge_cost
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    return None 


start, goal = 'A', 'E'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Path from {start} to {goal} with minimum path is: {path} with a cost of {cost}")