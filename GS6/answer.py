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


def cost(mat, n1, n2, n3, n4) -> int:
    """
    Returns cost difference for the 2 opt function
    """
    return mat[n1][n3] + mat[n2][n4] - mat[n1][n2] - mat[n3][n4]


def tsp(mat, start, best) -> int:
    '''
    :param mat: 2D matrix from input file
    :param start: Starting point from the best route generated by 2 opt
    :param best: best route generated from the 2 opt function
    :return: Minimum cost
    '''
    best_route = best
    k = start
    pathweight = 0
    for i in best_route:
        # for each point in the best route, generate the pathweight
        pathweight += mat[k][i]
        k = i
    pathweight += mat[k][start]
    min_path = pathweight
    return min_path


def opt2(route:[int], mat)->[int]:
    '''
    Two opt solution for minimizing distance
    :param route:
    :param mat: Matrix from the create_matrix function (distance matrix)
    :return: Approximate best sequence of points to visit
    '''
    best = route
    better = True
    while better:
        better = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                # Take the cost difference using the helper function and see if it is less than 0 (better)
                if cost(mat, best[i - 1], best[i], best[j - 1], best[j]) < 0:
                    best[i:j] = best[j - 1:i - 1:-1]
                    better = True
        route = best
    for i in best:
        print(i)
    return best


def create_matrix(files:[str]) -> [int]:
    '''
    Create cost matrix given the file input
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
    initial = list(range(length))
    best_route = opt2(initial, mat)
    # generate best sequence of points to visit from two opt function
    # then put into the tsp solver (adapted from my earlier brute force solution)
    print(tsp(mat, 0, best_route))










