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


def tsp(mat, start, size)->int:
    '''
    The most brute force solution I could think of to the travelling salesman problem (timed out the autograder though)
    :param mat: 2D matrix from input file
    :param start: Vertex 0
    :param size: Number of total verticies to visit
    :return: Minimum cost
    '''
    vertex = []
    for i in range(size):
        if i != start:
            vertex.append(i)
    next_permutation = permutations(vertex)
    last_path = []
    dict_of_indicies = dict()
    min_path = 0
    for i in next_permutation:
        current_pathweight = 0
        indicies = []
        k = start
        for j in i:
            current_pathweight += mat[k][j]
            # Store the indicies that go into the final solution so that we can print
            indicies.append(mat[k][j])
            k = j
        current_pathweight += mat[k][start]
        indicies.append(mat[k][start])
        if current_pathweight not in dict_of_indicies:
            # store the indicies at the key value of the current pathweight
            dict_of_indicies[current_pathweight] = indicies
        min_path = current_pathweight
        last_path.append(min_path)
        for path in last_path:
            # Check whether it is the minimum path
            if path < min_path:
                min_path = path
    for index in dict_of_indicies[min_path]:
        print(index)
    return min_path


def create_matrix(files:[str]):
    '''
    Create matrix
    :param files: File input
    :return: 2D matrix for TSP
    '''
    matrix = []
    for file in files:
        point = file.split()
        x = int(point[0])
        # Convert the point to an array and then add it to the matrix
        arr = [x]
        for item in point[1:]:
            # Convert strings to ints to make tsp operations easier
            arr.append(int(item))
        matrix.append(arr)
    return matrix


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    # Open the file and read in its contents
    with open(filename) as data_file:
        files = data_file.readlines()
        length = len(files)
    # Create matrix
    mat = create_matrix(files)
    # Print path & least cost
    print(tsp(mat, 0, length))









