"""
Author: swetha@udel.edu
Date: 2/18/2021
Description: CISC 320 Lesson 03: Using GradeScope
Takes a filename from stdin, loads it into an int
 array, and sums only the positive values
"""


def summation(lines: [int]) -> int:
    """
        Sums sequence of numbers while skipping negative numbers and stops upon
        encountering -999     """
    total = 0
    if len(lines) == 0:
        return "EMPTY"
    # store the first value in a variable so that we can subtract this from the sum later
    value = lines[0]
    value = int(value)

    for line in lines:
        line = int(line)
        if line == -999:
            if total - value <= 0:
                return "EMPTY"
            else:
                total = total - value
                return total
        if line >= 0:
            # only add nonnegative values to total
            total += line
    total -= value
    if total <= 0:
        return "EMPTY"
    return total


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
    value = summation(lines)
    print(value)
