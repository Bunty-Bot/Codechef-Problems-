Question:-
  Write a program to find the remainder when an integer A is divided by an integer B.
  
Input:-
  The first line contains an integer T, the total number of test cases. Then T lines follow, 
  each line contains two Integers A and B.
  
Output:-
  For each test case, find the remainder when A is divided by B, and display it in a new line.
  
Constraints:-
  1 ≤ T ≤ 1000
  1 ≤ A,B ≤ 10000
  
Example:-
Input
3 
1 2
100 200
40 15

Output
1
100
10

Code:-
  t = int(input())
  for i in range (t):
      str = input().split()
      a = int(str[0])
      b = int(str[1])
      c = int(a%b)
      print(c)
      
# This is the 6th problem in the beginner's section. This is nothig but we have to use modulus operator
# to solve this problem.
# if you like:
#    give star
# else:
#    give star