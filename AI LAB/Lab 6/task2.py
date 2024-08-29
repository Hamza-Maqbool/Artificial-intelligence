import heapq


graph = {
    'A': [('B', 3), ('F', 5)],
    'B': [('A', 3), ('C', 1), ('D', 7)],
    'C': [('B', 1), ('D', 2)],
    'D': [('B', 7), ('C', 2), ('E', 3)],
    'E': [('D', 3), ('J', 5)],
    'F': [('A', 5), ('G', 2)],
    'G': [('F', 2), ('H', 3)],
    'H': [('G', 3), ('I', 2)],
    'I': [('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}


h = {
    'A': 10,
    'B': 9,
    'C': 7,
    'D': 8,
    'E': 8,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 2,
    'J': 0
}

def a_star(graph, h, start, goal):
    queue = []  
    heapq.heappush(queue, (h[start], start, 0, [start]))  # (f, current_node, g, path)

    visited = set()

    while queue:
        f, current_node, g, path = heapq.heappop(queue)

        if current_node in visited:
            continue

        if current_node == goal:
            return g, path

        visited.add(current_node)

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in visited:
                g_new = g + edge_cost
                f_new = g_new + h[neighbor]
                heapq.heappush(queue, (f_new, neighbor, g_new, path + [neighbor]))

    return None  


start, goal = 'A', 'J'
cost, path = a_star(graph, h, start, goal)
print(f"Path from {start} to {goal} with minimum cost using A* is: {path} with a cost of {cost}"),