**Lesson 03: Using GradeScope**

Swetha Sankar 

CISC 320

***Problem***: Summate a sequence of numbers while 
skipping certain ones

***Solution***: In order to solve this problem,
I used Dr.Bart's example code (main function to read and store the file as an array) as
a starting point, and then wrote a summate function. The summate function stores the
first value (# of integers to read) in a variable, and 
subtracts this from the final sum after the other
values have been summed. The function checks whether
the list is empty, and if it is, then it returns the "EMPTY" string.
It then uses a for loop to decide which numbers to add to the total 
sum. It only adds numbers if they are >=0 (nonnegative), and also 
stops summing if it encounters the value -999. If it encounters -999, and the 
current sum (subtracting the first value) is 0, then it will return the string 
"EMPTY" because no suitable values were given. Else, it will return the current sum.
If it doesn't encounter -999, then it will go through all of the values in the list,
sum the nonnegative ones, subtract the first value, and return this total. This solution also
checks for the final sum being a positive value before returning the value. It then 
prints the returned value in the main function.

***Algorithmic Runtime***: This program uses a for loop to go through all of the 
elements in the list, so the runtime is O(n). It would be O(N) for the worst case (going through
all of the numbers in the list) and O(1) in the best case. 
