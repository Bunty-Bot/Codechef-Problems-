# Question:
#   Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. 
#   A triangle is valid if the sum of all the three angles is equal to 180 degrees.
  
# Input:
#   The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three angles 
#   A, B and C, of the triangle separated by space.
  
# Output:
#   For each test case, display 'YES' if the triangle is valid, and 'NO', if it is not, in a new line.
  
# Constraints:
#   1 ≤ T ≤ 1000
#   1 ≤ A,B,C ≤ 180
  
# Example:
#   Input
#   3 
#   40 40 100
#   45 45 90
#   180 1 1
#   Output
#   YES
#   YES
#   NO
  
# Code:
  t = int(input())
  for i in range(t):
      a,b,c = map(int, input().split())
      if a+b+c==180:
          print("YES")
      else:
          print("NO")
          
# This is the code for Valid triangle problem. This is one of the most eaisiest problem in the beginner's section. In this problem we just need to add
# one condition and then we are done with our program.
# if you like the code:
#   Give a star 
# else:
#   Give a star
