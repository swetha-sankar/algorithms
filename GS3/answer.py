"""
Author: swetha@udel.edu
Date: 3/10/2021
Description: CISC 320 Lesson 15: Graph Traversal
Problem: Find the last visited node in a traversal and calculate shortest path to it from certain other nodes.

Input: The filename of a local file containing a sequence of rooms and their neighbors, each on their own line.
The first line contains the number of rooms in the house, and is not included in the number of vertices.
You can assume that each line will contain only one room's information. The lines are ordered alphabetically by the name
of the room. The neighbors within a line are also ordered alphabetically.

Output: A series of paths that the robots will take.
Each robot's path should be printed on its own line, with the room names
separated by spaces. The path should be given from the robot's room to Dr. Bart's room.
Report the paths in alphabetical order by the robot's room name.
"""
from collections import deque


def bfs(s, e, adj):
    '''
    :param s: Takes in the starting room key
    :param e: Takes in the ending room key (Dr. Bart's location)
    Short helper function for executing BFS algorithm. Calls solve & build and prints output returned from build
    '''
    path = []
    prev = solve(s, adj)
    path = build(s, e, prev)

    for room in path:
        print(room, end=' ')
    print(' ')

    return path


def find_bart(s, adj):
    '''
    Method to return the room that Dr.Bart is in (the last room visited by BFS)
    :param s: Takes in the starting room key
    :return: Returns the last room visited by BFS
    '''
    q = deque()
    # queue implementation w/ deque
    visited = [s]
    prev = dict()
    q.append(s)
    while len(q) > 0:
        node = q.popleft()
        neighbors = adj[node]
        for i in neighbors:
            if i not in visited:
                q.append(i)
                visited.append(i)
                prev.__setitem__(i, node)
    return visited[-1]


def solve(s, adj):
    '''
    :param s: Takes in the starting room key
    :return: Returns a dictionary of the previous paths
    '''
    q = deque()
    visited = [s]
    prev = dict()
    q.append(s)
    while len(q) > 0:
        node = q.popleft()
        neighbors = adj[node]
        for i in neighbors:
            if i not in visited:
                q.append(i)
                visited.append(i)
                prev.__setitem__(i, node)
    return prev


def build(s, e, prev):
    '''

    :param s: Starting room key
    :param e: Ending room key
    :param prev: Dictionary of previous paths from solve method
    :return:
    '''
    path = []
    at = e
    # build path backwards
    while at is not None:
        path.append(at)
        at = prev.get(at)
    path.reverse()
    if path[0] == s:
        # check if start & end connected
        return path
    return []


def map_lines(lines: [str]):
    '''

    :param lines: Takes in array of strings (individual file lines w/ comma-separation)
    :return: Dictionary with room name as key and values of room neighbors and robot string
    '''
    rooms = dict()
    for line in lines[1:]:
        line = line.split()
        # key: room name, values: [adjacent rooms], robot/empty string
        if line[0] not in rooms:
            rooms[line[0]] = [line[2:]]
            rooms[line[0]].append(line[1])
    return rooms


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        # O(L) operation
        files = data_file.readlines()
        start = files[1].split()[0]

    # Room_dict: Key = Room name. Values = neighbors in tuple, string of robot/empty.
    room_dict = map_lines(files)

    # adj = Adjacency list that is used for BFS. Passed into BFS, solve, and find_bart methods
    adj = dict()
    robos = []
    for key in room_dict:
        # from mapped lines, form robo key list (for later) and also make the adjacency list for bfs
        adj[key] = room_dict[key][0]
        if room_dict[key][1] == "robot":
            robos.append(key)
    # the find_bart method will return the key of the last room the alg visits (location of dr. bart)
    dr_bart = find_bart(start, adj)
    for robo in robos:
        # goes from each robot start to dr_bart (bfs takes params of start and end node)
        # the bfs method uses the start method & reconstruct path method in order to find the shortest path
         bfs(robo, dr_bart, adj)
