Question:
  If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.
  
Input:
The first line contains an integer T, the total number of test cases. 
Then follow T lines, each line contains an integer N.

Output:
For each test case, display the sum of first and last digits of N in a new line.

Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000

Example:
Input
3 
1234
124894
242323

Output
5
5
5

Code:
  t = int(input())
  for i in range(t):
      num = input()
      sum = int(num[0])+int(num[-1])
      print(sum)
      
# This is the code for the First and Last Digit problem. This is the 8th problem in beginner's section.
# if you like:
#    give star
# else:
#   give star
