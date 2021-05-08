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
from itertools import permutations
from sys import maxsize


def tsp(mat, start, size):
    # This probably has terrible runtime because it just permutes all combinations of the verticies and
    # calculates the weight... just want to test against the baseline
    vertex = []
    for i in range(size):
        if i != start:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = start
        for j in i:
            current_pathweight += mat[k][j]
            k = j
        current_pathweight += mat[k][start]
        min_path = min(min_path, current_pathweight)
    return min_path


def create_matrix(files:[str]):
    # create 2d matrix given the file input
    matrix = []
    for file in files:
        point = file.split()
        x = int(point[0])
        point_as_array = [x]
        for thing in point[1:]:
            point_as_array.append(int(thing))
        matrix.append(point_as_array)
    return matrix


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    # Open the file and read in its contents
    with open(filename) as data_file:
        files = data_file.readlines()
        len = len(files)
    mat = create_matrix(files)
    # Create the adjacency matrix
    print(tsp(mat, 0, len))









