Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.  

Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.  

Example 1:
```buildoutcfg
Input:
    A = ["hello", "scaler", "interviewbit"]
    B = "adhbcfegskjlponmirqtxwuvzy"
Output:
    is_dictionary = 1
```

Example 2:
```buildoutcfg
Input:
    A = ["fine", "none", "no"]
    B = "qwertyuiopasdfghjklzxcvbnm"
Output:
    is_dictionary = 0
```