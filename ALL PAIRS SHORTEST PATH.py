def floyd_warshall(graph):
    n = len(graph)

    distance = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != float('inf') and distance[k][j] != float('inf'):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        print("\nThrough", k + 1, ":")
        for row in distance:
            print(row)

    return distance

n = int(input("Enter number of vertices: "))
adjacency_matrix = [[float('inf')] * n for _ in range(n)]

print("Enter the graph (enter 'inf' for infinity):")
for i in range(n):
    for j in range(n):
        while True:
            try:
                value = input(f"Weight from vertex {i + 1} to {j + 1}: ")
                if value.lower() == 'inf':
                    adjacency_matrix[i][j] = float('inf')
                else:
                    adjacency_matrix[i][j] = int(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer or 'inf'.")

print("Initial Distance Matrix:")
for row in adjacency_matrix:
    print(row)

result = floyd_warshall(adjacency_matrix)

print("\nFinal Distance Matrix:")
for row in result:
    print(row)
