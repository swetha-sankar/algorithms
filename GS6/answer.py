'''
Swetha Sankar
Lesson 25: Approximation
Problem: Find the approximately shortest path that visits every vertex and returns to the first one.

Input: The filename of a local file containing a sequence of distances in a 2D matrix.
Every line consists of N numbers, and there are N lines.
Each individual number represents the distance between the vertices given by the indices of the matrix.

Output: The sequence of indices chosen to minimize the total distance travelled, and the
calculated total cost of that tour.
'''
from itertools import combinations


def tsp(m, S):
    N = m.size
    memo = t = [[-1 for i in range(N + 1)] for j in range(N + 1)]
    setup(m, memo, S, N)
    solve(m, memo, S, N)
    minCost = findMinCost(m, memo, S, N)
    tour = findOptimalTour(m, memo, S, N)
    return (minCost, tour)

def setup(m, memo, S, N):
    for i in range(N):
        if i == S:
            continue
        memo[i][i << S | 1 << i] = m[S][i]

def solve(m, memo, S, N):
    for i in range(3, N):
        for subset in combinations(i, N):
            if S not in subset:
                continue
            for next in range(N):
                if next == S or next not in subset:
                    continue
                state = subset ^ (1 << next)
                minDist = +float('inf')

if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    # Open the file and read in its contents
    with open(filename) as data_file:
        files = data_file.readlines()
        len = len(files)
    # Create the adjacency matrix
    matrix = []
    for file in files:
        point = file.split()
        x = int(point[0])
        point_as_array = [x]
        for thing in point[1:]:
           point_as_array.append(int(thing))
        matrix.append(point_as_array)
    print(matrix)
    tsp(matrix, matrix[0])








