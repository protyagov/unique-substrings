# Unique Substrings in Wraparound Strings

For lower case english string p find how many unique non-empty substrings of p are present in endless wraparound string of form "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 


*Examples:*
```
  Input: "a"
  Output: 1
  Explanation: Only the substring "a" of string "a" is in the string s.
 
  Input: "cac"
  Output: 2
  Explanation: There are two substrings "a", "c" of string "cac" in the string s.

  Input: "zaba"
  Output: 6
  Explanation: There are 6 substrings: a, b, z, ab, za, zab
```
**Observation**
```
Number of matches = number of previous matches + number of letters in the sequence.

1 chars -->  1 match
2 chars -->  3 matchs  ==  2 + 1
3 chars -->  6 matchs  ==  3 + 3
4 chars --> 10 matchs  ==  4 + 6
5 chars --> 15 matchs  ==  5 + 10
6 chars --> 21 matchs  ==  6 + 15
7 chars --> 28 matchs  ==  7 + 21
8 chars --> 36 matchs  ==  8 + 28 

```

**Algorithm** 

There are only 26 possible sequences that start from the same letter. Larger sequence always contains all combinations of its subsequences hence we look for the largest sequence and assign its count to the corresponding letter in the 26 letter bucket. At the end we sum counts from 26 buckets to get our answer.

Start at i = 0 and go forward until first out of order char. That be postion j. So subsequece i to j is valid. Using above observation calculate number of marches for letter at i = 0, which is j - i. Number of matches for a letter at i+1 is one step less than and so on until we get to j, which is just 1. Now we have processed all possible combinations between i and j. We can skip all chars until j and process next sequence.


**Runtime** 

Above solution runs at linear time, **O(n)** becaue we visti each character in the string p eaxactly once. Solution is memory eficient because it only uses 26 buckets to hold sums for each possible max sequence plus a few counters and string itself.


LeetCode says my solution is faster than 80% of online submissions in a pool of 23,790 solutions, and uses 100% less memory among them.

![Image of Yaktocat](https://github.com/protyagov/unique-substrings/blob/master/leetcode.png)
