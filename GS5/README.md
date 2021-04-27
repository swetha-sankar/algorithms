**Lesson 21: Bookbag Filling**

Swetha Sankar 
CISC 320
April 26, 2021

***README.md:*** Describes solution, relevant files, algorithmic runtime

**Relevant Files:**
answer.py: Contains all functions and driver code for project
test.py: Contains any testing cases I used for individual functions

**Solution:**
Used the knapsack 0/1 video in the lesson as a starting point for the logic to create the 2D matrix and 
dynamically program the solution. Converting the files to a list is an O(n) operation.
I take the files and convert them to three arrays: one for storing the
names of the items, one for storing the values, and one for storing the weights of the items. This
is an O(1) operation. I then initialize a 2D array with n+1 rows and W+1 columns and pass this into my knapsack function, which builds the 2D array
from the bottom up. This has a time complexity of O(nW) where n is the number of items
and W is the capacity. This is because we use the array to store all subproblems, and we reuse the subproblems
to ultimately solve the final problem of the optimal subset. This solution also uses space of O(nW) as the 2D array is 
initialized to this size. 
This solution uses pseudo-polynomial time (O(nW)) since 
the capacity W only needs log W bits to describe (https://en.wikipedia.org/wiki/Pseudo-polynomial_time).
The use of dynamic programming and saving previous solutions in a 2D array keeps this complexity at O(nW) instead of
O(2^n) that a greedy approach would use (http://cse.unl.edu/~goddard/Courses/CSCE310J/Lectures/Lecture8-DynamicProgramming.pdf).




