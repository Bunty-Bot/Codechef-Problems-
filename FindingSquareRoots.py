# Question:
#   In olden days finding square roots seemed to be difficult but nowadays 
#   it can be easily done using in-built functions available across many languages .
#   Assume that you happen to hear the above words and you want to give a try in finding 
#   the square root of any given integer using in-built functions. So here's your chance.
  
# Input:
#   The first line of the input contains an integer T, the number of test cases. T lines follow. 
#   Each line contains an integer N whose square root needs to be computed.
  
# Output:
#   For each line of the input, output the square root of the input integer, rounded down to 
#   the nearest integer, in a new line.
  
# Constraints:
#   1<=T<=20 
#   1<=N<=10000
  
# Example:
#   Input:
#   3
#   10
#   5
#   10000

#   Output:
#   3
#   2
#   100
  
# Code:
  t = int(input())
  for i in range(t):
      num = int(input())
      sqrt = int(num**0.5)
      print(sqrt)
      
# This is the 12th problem in the beginner's section. This is a very easy problem
# In this problem we have to find the squareroot of the numbers but the result should 
# be in integer form.
