Given an array of integers, find the noble element.
A noble element is an integer P such that there are exactly P number of elements in the array that are greater than P.

If there exists such a noble element return the element else return -1


Example 1:
```buildoutcfg
Input:
    arr = [3,2,1,4]
Output:
    P = 2
Explanation:
    Number of elements greater than P = [3,4]
```

Example 2:
```buildoutcfg
Input:
    arr = [1,2,3,4,5]
Output:
    P = -1
Explanation:
    There is no such value that satisfies the noble element condition.
```