<h1> Runtime Complexity</H1>
Converting the file to a list is an O(L) operation. 
My program then takes the list and converts
it to a dictionary of a dictionary of student results. This
is a an O(L) operation. Sorting this dictionary is
an O(S * log(S)) operation where S = number of students. Printing
the dictionary is an O(S) operation. 
This simplifies to O(L+L+S*log(s)+S) which
simplifies to O(L+S*log(S)) for the expected case.

