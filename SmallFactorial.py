Question:
  Write a program to find the factorial value of any number entered by the user.
  
Input:
  The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.
  
Output:
  For each test case, display the factorial of the given number N in a new line.
  
Constraints:
  1 ≤ T ≤ 1000
  0 ≤ N ≤ 20
  
Example:
  Input
  3 
  3 
  4
  5

  Output

  6
  24
  120
  
Code:
  def fact(n):
      ans=1
      for i in range(1,n+1):
           ans=ans*i
      return(ans)
  t=int(input())
  for i in range(t):
      n=int(input())
      print(fact(n))
      
# This is the code for small factorial problem. This is the basic and most common question which we get while learning any language.
# Due to popularity of this question this is the easy question in the beginner's section. We can do this by importing maths module,
# or by recursive approach or by iterative approach.
# if you like the code:
#   Give a star
# else:
#   Give a star
