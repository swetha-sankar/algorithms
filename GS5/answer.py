'''
Swetha Sankar
Lesson 21: Bookbag Filling
April 23, 2021
Problem: Identify the subset of items that will maximize their value while keeping their total weight equal to or below a threshold.

Input: The filename of a local file containing a sequence of items, each on their own line. The first line contains the
number of total items in the facility. The second line specifies the maximum capacity of the bookbag. All subsequent lines
describe the sequence of items and contain three elements: Name Weight Value


'''

def map_lines(lines: [str]):
    """
       Format lines in the input so that we know what values are the names/weights/values
       """
    items = dict()
    for line in lines[2:]:
        # format line split to make accessing elements easier
        name, weight, value = line.split()
        weight = int(weight)
        value = int(value)
        if name not in items:
            # key = name of item, values = [weight, value]
            items[name] = [weight, value]
    return items


def create_wt(mapped):
    # create array of weights
    weights = []
    for key in mapped_items:
        weights.append(mapped_items[key][0])
    return weights


def create_val(mapped):
    # create array of values
    values = []
    for key in mapped_items:
        values.append(mapped_items[key][1])
    return values


def knapsack(wt, val, capacity, items, t):
    # base cases
    if items == 0 or capacity == 0:
        return 0
    if t[items][capacity] != -1:
        return t[items][capacity]

    if wt[items - 1] <= capacity:
        t[items][capacity] = max(val[items - 1] +
                                 knapsack(wt, val, capacity - wt[items - 1], items - 1, t),
                                 knapsack(wt, val, capacity, items - 1, t))
        return t[items][capacity]
    elif wt[items - 1] > capacity:
        t[items][capacity] = knapsack(wt, val, capacity, items - 1, t)
        return t[items][capacity]


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    # Open the file and read in its contents
    with open(filename) as data_file:
        files = data_file.readlines()
        numItems = int(files[0])
        capacity = int(files[1])

    # Actually do the work
    mapped_items = map_lines(files)
    val = create_val(mapped_items)
    wt = create_wt(mapped_items)

    # initialize 2D matrix to all -1 values
    t = [[-1 for i in range(capacity + 1)] for j in range(numItems + 1)]
    print(knapsack(wt, val, capacity, numItems, t))



