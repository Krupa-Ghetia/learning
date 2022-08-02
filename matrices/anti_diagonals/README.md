Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.  
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.  

Example 1:
```buildoutcfg
Input:
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Output:
    result = [[1,0,0,0],[2,5,0,0],[3,6,9,0],[4,7,10,13],
              [8,11,14,0],[12,15,0,0],[16,0,0,0]]
```

Example 2:
```buildoutcfg
Input:
    mat = [[1,2],[3,4]]
Output:
    result = [[1,0],[2,3],[4,0]]
```