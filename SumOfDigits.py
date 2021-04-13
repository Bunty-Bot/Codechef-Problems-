# Question:-
#   You're given an integer N. Write a program to calculate the sum of all the digits of N.
  
# Input:-
#   The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.
  
# Output:-
#   For each test case, calculate the sum of digits of N, and display it in a new line.
  
# Constraints:-
#   1 ≤ T ≤ 1000
#   1 ≤ N ≤ 1000000
  
# Example:-
#   Input
#   3 
#   12345
#   31203
#   2123
#   Output
#   15
#   9
#   8

# Code:-
  t = int(input())
  for i in range(t):
      sum = 0
      n = int(input())
      while n!=0:
          m=n%10
          sum = sum + m
          n = n//10
      print(sum)
      
#This is the 5th problem in the beginner's section. This is kind of a challenging problem for the beginner but if your concepts
#are clear then this problem will be easy to you. This problem needs a good knowledge of loops.
