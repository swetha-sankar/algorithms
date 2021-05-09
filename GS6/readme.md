**Lesson 25: Approximation**

Swetha Sankar 
CISC 320-010
May 9, 2021

***README.md:*** Describes solution, relevant files, algorithmic runtime

**Relevant Files:**
answer.py: Contains all functions and driver code for project
input.txt/input2.txt: Testing examples for checking functionality of main function
test.py: Testing cases 

**Solution:**
I used the linked resources in the assignment as a starting point, and developed my solution by first converting the file input to a cost matrix
(create_matrix method), and then used this matrix within a 2-opt solution, which prints an improved order of verticies to visit.
We pass the original order of vertices into the 2 opt function (ex. [0,1,2,3,4,5]) and it checks to see whether a swapped path can improve the cost. 
It takes a route that crosses over itself and reorders it without the overlap. I then pass the improved route, the original matrix, and the starting
point of the improved route into the TSP cost generator (tsp function) which uses the matrix to generate the total cost of visiting the 
verticies in that order. This function simply traverses through the 2D matrix and adds together all of the costs.
I believe the two opt solution considers all of the pairs of edges in order to find improvement and this would be O(n^2) where n is the number of 
vertices. 

*Resources Used*
https://link.springer.com/article/10.1007/s00453-013-9801-4
http://pedrohfsd.com/2017/08/09/2opt-part1.html
https://stackoverflow.com/questions/53275314/2-opt-algorithm-to-solve-the-travelling-salesman-problem-in-python
https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/



