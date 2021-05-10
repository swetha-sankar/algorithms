**Lesson 15: Graph Traversal**

Swetha Sankar 
CISC 320
April 7, 2021

***README.md:*** Describes solution, relevant files, algorithmic runtime

**Relevant Files:**
answer.py: Contains all functions and driver code for project
testing.py: Contains any testing cases I used for individual functions

**Solution:**
Used the Breadth First Traversal (BFS) video linked in the assignment as a starting point, and developed my 
solution by converting the file input to a dictionary, converting that dictionary to an adjacency list, running that list 
through BFS to find Dr.Bart's room, and then running it through BFS again to find the shortest paths to Dr.Bart for each 
robot. My program then prints out the robot paths in alphabetical order (based on Robot starting room).

**Algorithmic Runtime**: 
This program runs in O(RE+RV) where R is the number of robots, V is the number of rooms, and E is the number of connections.
The program reads in the files which is an O(V) operation and converts them to a dictionary where the key is the room string and its values
are a list of neighbors as well as a robot string. It then traverses this dictionary to create an adjacency
list dictionary as well as a list to store any keys with robots in them. 
Iterating over a dictionary takes O(V) time in total, or on average O(1) time per element, 
where V is the number of rooms in the dictionary. I then conduct a breadth first search in order to find the room 
Dr. Bart is in using the adjacency list and a starting node, and then another breadth-first search for each robot in the list.
Breadth-first search has a running time of O(V+E) since every vertex and every edge will be checked once. Since we are 
conducting at most R+1 searches (# robots + initial search), this would simplify to O(RE+RV).


