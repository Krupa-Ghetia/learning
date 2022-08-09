Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single element "-1".

First sub-array means the sub-array for which starting index in minimum.  

Example 1:
```buildoutcfg
Input:
    A = [1,2,3,4,5]
    B = 5
Output:
    result = [2, 3]
```

Example 2:
```buildoutcfg
Input:
    A = [5,10,20,100,105]
    B = 110
Output:
    result = [-1]
```