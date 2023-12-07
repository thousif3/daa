import heapq 

class Solution: 
    def spanningTree(self, V, adj): 
        pq = [(0, 0)]  # (wt, node) 
        vis = [0] * V 
        sum = 0 

        while pq: 
            wt, node = heapq.heappop(pq) 

            if vis[node] == 1: 
                continue 

            vis[node] = 1 
            sum += wt 

            for neighbor in adj[node]: 
                adjNode, edW = neighbor[0], neighbor[1] 
                if not vis[adjNode]: 
                    heapq.heappush(pq, (edW, adjNode)) 

        return sum 

V = 5 
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]] 
adj = [[] for _ in range(V)] 
for it in edges: 
    adj[it[0]].append([it[1], it[2]]) 
    adj[it[1]].append([it[0], it[2]]) 

obj = Solution() 
result = obj.spanningTree(V, adj) 
print("The sum of all the edge weights:", result)



    

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_vertex = 'A'
    result = dijkstra(graph, start_vertex)

    print(f"Shortest distances from {start_vertex}: {result}")
    
    
    
    

    
    
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': -1, 'D': 1},
    'C': {'B': 3, 'D': 2},
    'D': {'C': -3}
}

start_node = 'A'
distances = bellman_ford(graph, start_node)

print(distances)












n = 4
INF = float('inf')
def floyd_warshall(G):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j],G[i][k] + G[k][j])
    print_solution(G)
def print_solution(distance):
    for i in range(n):
        for j in range(n):
            print(distance[i][j], end="  ")
        print(" ")
G = [[0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]]
floyd_warshall(G)
    
