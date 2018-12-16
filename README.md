# find_sum
Q:
Given a sorted array of integers and a variable n, please write an algorithm to find out all
pairs in the array that sum value equal to n. For example,
given [1, 2, 3, 5, 7, 8, 9, 9] and n=10,
you should output [1,9], [1,9], [2,8], [3,7]
Please write the code and related test cases.
A:
First: Check weather the parameters are valid;
Second: Put the list into a dict, Set the key to sum_num-list[i] and the value to list[i]
Third: Traveling the dict and find the valid key-value and put it into a list
Last: Output the list and split it with ','

The time complexity is O(n).
