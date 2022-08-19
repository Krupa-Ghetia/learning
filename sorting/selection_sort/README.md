Given an integer array A of size N.

You need to sort the elements in increasing order using SelectionSort. Return a array containing the min value's index position before every iteration.

NOTE:
* Consider 0 based indexing while looking for min value in each step of selection sort.
* There will be total N - 1 iterations in selection sort so the output array will contain N - 1 integers.

Example:
```buildoutcfg
Input:
    A = [6,4,3,7,2,8]
Output:
    result = [4,2,2,4,4]
```

Explanation:
Before 1st iteration: [6,4,3,7,2,8] -- Index of 1st min is 4
After 1st Iteration: [2,4,3,7,6,8] -- Index of 2nd min is 2
After 2nd Iteration: [2,3,4,7,6,8] -- Index of 3rd min is 2
After 3rd Iteration: [2,3,4,7,6,8] -- Index of 4th min is 4
After 4th iteration: [2,3,4,6,7,8] -- Index of 5th min is 4
After 5th iteration: [2,3,4,6,7,8]