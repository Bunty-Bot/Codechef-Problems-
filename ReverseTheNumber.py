# Question:
#   Given an Integer N, write a program to reverse it.
 
# Input:
#   The first line contains an integer T, total number of testcases. Then follow T 
#   lines, each line contains an integer N.
  
# Output:
#   For each test case, display the reverse of the given number N, in a new line.
  
# Constraints:
#   1 ≤ T ≤ 1000
#   1 ≤ N ≤ 1000000
  
# Example:
#   Input
#   4
#   12345
#   31203
#   2123
#   2300
#   Output
#   54321
#   30213
#   3212
#   32
  
# Code:
  t = int(input())
  for i in range(t):
      a = input()
      str = a[::-1]
      str = int(str)
      print(str)
      
# This is the code for Reverse The Number problem. This is the 11th problem in the beginner's section.
# In this problem we have to print the reverse order of the number which was given by the user.
# if you like it:
#   give a star
# else:
#   give a star
