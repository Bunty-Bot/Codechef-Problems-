# Question:
#   Write a program to obtain a number N
#   and increment its value by 1 if the number is divisible by 4 otherwise
#   decrement its value by 1.
  
# Input:
#   First line will contain a number N.
  
# Output:
#   Output a single line, the new value of the number.
  
# Constraints:
#   0≤N≤1000
  
# Example:
#   Sample Input:
#   5
#   Sample Output:
#   4
  
# Explanation:
#   Since 5 is not divisible by 4 hence, its value is decreased by 1.
  
# Code:
  N = int(input())
  if N%4==0:
      N = N + 1
      print(N)

  else:
      N = N -1
      print(N)
