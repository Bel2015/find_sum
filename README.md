# find_sum
Q:
Given a sorted array of integers and a variable n, please write an algorithm to find out all
pairs in the array that sum value equal to n. For example,
given [1, 2, 3, 5, 7, 8, 9, 9] and n=10,
you should output [1,9], [1,9], [2,8], [3,7]
Please write the code and related test cases.
A:
First: Check weather the parameters are valid;
Second: Select the first element in the list and the elements after it ,if the sum of them is equal to the sum number,  put them into a list. Then the second, and so on.
Last: Output the list and split it with ',', the boundary of the output can't be ','

The time complexity is O(n*n).
