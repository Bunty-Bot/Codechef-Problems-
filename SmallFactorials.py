Question:-
  You are asked to calculate factorials of some small positive integers.
  
Input:-
  An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, 
  each containing a single integer n, 1<=n<=100.
  
Output:-
  For each integer n given at input, display a line with the value of n!
  
Example:-
  Sample input:
  4
  1
  2
  5
  3
  Sample output:

  1
  2
  120
  6
  
Code:-
  t = int(input())
  for i in range(t):
      n = int(input())
      fact = 1
      for i in range(1,n+1):
          fact = fact*i
      print(fact)
      
      
# This is the 7th problem in the beginner's section. This quite tough as compare to other problems.
# But if you have a good knowledge of math then it is easy.
# If you like:
#    give a star
# else:
#    give a star
