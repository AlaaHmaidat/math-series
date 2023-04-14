# Math Series

numeric series starting with the integers n and m. In this series, the next integer is determined by summing the previous two. Like Fibonacci Series and Lucas Numbers.

Fibonacci Series start with the integers 0 and 1. The resulting series looks like this:
0, 1, 1, 2, 3, 5, 8, 13, ...

Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...

## Approach & Efficiency

1. Create a function. 
2. The function have one required parameter n. 
3. The function return the nth value in the series using recursion.

 The time complexity of the function is O(2^n), which means that the running time grows exponentially with the size of the input n. This is because the function recursively calls itself twice for each value of n greater than or equal to 2.

 The space complexity is also O(2^n), as the function creates a recursive call stack with a depth proportional to the input n.

## Solution
Click [here](./series/series.py) to see the solution