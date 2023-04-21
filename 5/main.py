import itertools
import numpy as np

def isomorphic(graph1, graph2):
    if np.shape(graph1) != np.shape(graph2):
        return False

    num = len(graph1)
    for perm in itertools.permutations(range(num)):
        valid = True
        checking = {}

        for i in range(num):
            for j in range(num):
                if graph1[i][j] != graph1[perm[i]][perm[j]]:
                    valid = False
                    break
            if not valid:
                break

            # Записуємо відповідність між вершинами графів
            checking.setdefault(graph1[i][i], graph2[perm[i]][perm[i]])
            if checking[graph1[i][i]] != graph2[perm[i]][perm[i]]:
                valid = False
                break

        if valid:
            return True

    return False

with open('graph2.txt') as file:
    adjacency_matrix1 = np.loadtxt(file, dtype=int)
    print(f"\nAdjacency matrix 1:\n{adjacency_matrix1}")
with open('graph1.txt') as file:
    adjacency_matrix2 = np.loadtxt(file, dtype=int)
    print(f"\nAdjacency matrix 2:\n{adjacency_matrix2}")

if isomorphic(adjacency_matrix1, adjacency_matrix2):
    print("\nIsomorphism exist.")
else:
    print("\nIsomorphism do not exist.")