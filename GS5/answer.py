'''
Swetha Sankar
Lesson 21: Bookbag Filling
April 23, 2021
Problem: Identify the subset of items that will maximize their value while keeping their total weight equal to or below a threshold.

Input: The filename of a local file containing a sequence of items, each on their own line. The first line contains the
number of total items in the facility. The second line specifies the maximum capacity of the bookbag. All subsequent lines
describe the sequence of items and contain three elements: Name Weight Value

Solution: Finds the subset of items that maximize value while keeping <= threshold capacity
Prints out the list of items and their total value

'''


def knapsack(wt: [int], val: [int], capacity: int, items: int, t, name: [str]) -> int:
    '''
    Builds 2D matrix for dynamic programming and prints optimal subset of items for Babbage to fill his bookbag
    :param wt: Array of weights
    :param val: Array of values
    :param capacity: Total capacity
    :param items: Total number of items
    :param t: 2D matrix for storing previous values
    :param name: Array of names of items
    :return: int: Total value of items within subset
    '''
    if items == 0 or capacity == 0:
        return 0
    # Create 2D array by taking into account values and weights
    for i in range(items + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i - 1] <= j:
                t[i][j] = max(val[i - 1]
                              + t[i - 1][j - wt[i - 1]],
                              t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    result = t[items][capacity]
    # Store final value of items within subset to print later
    ans = t[items][capacity]
    x = capacity
    # Print each item in knapsack
    for i in range(items, 0, -1):
        if result <= 0:
            break
        if result == t[i - 1][x]:
            continue
        else:
            # The item is in the subset
            print(name[i - 1])
            result = result - val[i - 1]
            x = x - wt[i - 1]
    print(ans)
    # Return for testing purposes
    return ans


def split_names(lines: [str])->[str]:
    # create array of names
    names = []
    for line in lines[2:]:
        name, weight, value = line.split()
        names.append(name)
    return names


def split_weights(lines: [str])->[int]:
    # create array of weights
    weights = []
    for line in lines[2:]:
        name, weight, value = line.split()
        weights.append(int(weight))
    return weights


def split_values(lines: [str])->[int]:
    # create array of values
    values = []
    for line in lines[2:]:
        name, weight, value = line.split()
        values.append(int(value))
    return values


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    # Open the file and read in its contents
    with open(filename) as data_file:
        files = data_file.readlines()
        numItems = int(files[0])
        capacity = int(files[1])

    # Actually do the work
    val = split_values(files)
    wt = split_weights(files)
    name = split_names(files)

    # initialize 2D matrix to all -1 values
    t = [[-1 for i in range(capacity + 1)] for j in range(numItems + 1)]
    knapsack(wt, val, capacity, numItems, t, name)



