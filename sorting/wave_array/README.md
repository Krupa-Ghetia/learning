Given an array of integers A, sort the array into a wave-like array and return it.
In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5.....  
NOTE: If multiple answers are possible, return the lexicographically smallest one.

Example 1:
```buildoutcfg
Input:
    A = [1,2,3,4]
Output:
    A = [2,1,4,3]
```

Example 2:
```buildoutcfg
Input:
    A = [1,2]
Output:
    A = [2,1]
```

Explanation:

Example 1:  
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
First answer is lexicographically smallest. So, return [2, 1, 4, 3].

Example 2:  
Only possible answer is [2, 1].