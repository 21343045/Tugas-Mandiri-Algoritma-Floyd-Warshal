# Fungsi untuk mencetak matriks adjacency
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Algoritma Warshall
def warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
    return graph

# Algoritma Floyd
def floyd(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

# Contoh penggunaan
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

print("Matriks adjacency awal:")
print_matrix(graph)

print("Hasil algoritma Warshall:")
print_matrix(warshall(graph))

print("Hasil algoritma Floyd:")
print_matrix(floyd(graph))
