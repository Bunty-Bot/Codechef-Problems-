Question:
  Write a program, which takes an integer N and if the number is less than 10 then display "Thanks for helping Chef!" otherwise print "-1".
  
Input:
  The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
  
Output:
  For each test case, output the given string or -1 depending on conditions, in a new line.
  
Constraints:
  1 ≤ T ≤ 1000
  -20 ≤ N ≤ 20
  
Example:
  Input
  3 
  1
  12
  -5
  Output
  Thanks for helping Chef!
  -1
  Thanks for helping Chef!
  
Code:
  t=int(input())
  for i in range(t):
      n=int(input())
      if n<10:
          print('Thanks for helping Chef!')
      else:
          print(-1)
          
#  This is the code for Helping Chef problem. This is one of the most easiest problem for any beginner. But there is a problem in this problem.
# You should be careful while writing 'Thanks for helping Chef!' Because I forgot to give the exclamation mark after end of the sentence and 
# due to this even I wrote perfect code it was not accepting it. So be careful while solving any problem.
# if You like the code:
#   Give a star
# else:
#   Give a star
