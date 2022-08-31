Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.  

Example 1:
```buildoutcfg
Input:
    A = [2,1]
Output:
    cost = 4
```
Explanation: Given array A = [2, 1]  
Remove 2 from the array => [1].  
Cost of this operation is (2 + 1) = 3.

Example 2:
```buildoutcfg
Input:
    A = [5]
Output:
    cost = 5
```
Explanation: There is only one element in the array. So, cost of removing is 5.