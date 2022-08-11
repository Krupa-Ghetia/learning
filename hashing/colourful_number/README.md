Given a number A, find if it is COLORFUL number or not.

If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.  

Example 1:
```buildoutcfg
Input:
    A = 23
Output:
    result = 1
Explanation:
    subseq = [2,3,23]
    possible_products = {2:1, 3:1, 6:1}
```

Example 2:
```buildoutcfg
Input:
    A = 236
Output:
    result = 0
Explanation:
    subseq = [2,3,6,23,36,236] 
    possible_products = {2:1, 3:1, 6:2, 18:1, 36:1}
```