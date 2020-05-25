# sudoku
Backtrack Algorithm to solve Sudoko game on 9x9 board. 

**Sudoku1.py** 
  1. Start with last empty cell 
  2. Find all possible numbers we can put there
  3. Put first number from step 2.
  4. Go to another empty cell and repeat steps 2 & 3
  5. If we still have empty cells and there are no possible solution for current cell -- **backtrack**


**Sudoku2.py** 
This is extencion of the first solution. I have added *memoization* to reduce timing of step 2. We can only calculate available numbers for given empty cell once and then refer to it. Hence it is an example of *dynamic programming* because the occurences of the numbers are looked up.

According to LeetCode second solution performs 3x times faster than first one, and overall 83% faster among 176,000 acceptable submitted solutions.

![Image of Yaktocat](https://github.com/protyagov/unique-substrings/blob/master/leetcode.png)
