def bellman_ford(matrix, source):
    vertices = len(matrix)
    dist = [float('inf')] * vertices
    dist[source] = 0

    for _ in range(vertices - 1):
        print("\n\nRelation iteration ", _ + 1, ":")
        for u in range(vertices):
            for v in range(vertices):
                if matrix[u][v] != 0:
                    if dist[u] + matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + matrix[u][v]
                        print("After relaxation of (", u + 1, ",", v + 1, ") edge: ", dist)

    for u in range(vertices):
        for v in range(vertices):
            if matrix[u][v] != 0:
                if dist[u] + matrix[u][v] < dist[v]:
                    raise ValueError("Graph contains a negative cycle")
    return dist

N = int(input("Enter the number of vertices: "))
G = []

print("Enter adjacency matrix:")
for _ in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    
result = bellman_ford(G, 0)

for i in range(len(result)):
    print(f"Vertex {i + 1}: Distance = {result[i]}")
