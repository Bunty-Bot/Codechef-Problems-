Question:
  Three numbers A, B and C are the inputs. Write a program to find second largest among them.
  
Input:
  The first line contains an integer T, the total number of testcases. Then T lines follow, 
  each line contains three integers A, B and C.
  
Output:
  For each test case, display the second largest among A, B and C, in a new line.
  
Constraints:
  1 ≤ T ≤ 1000
  1 ≤ A,B,C ≤ 1000000
  
Example:
  Input
  3 
  120 11 400
  10213 312 10
  10 3 450

  Output

  120
  312
  10
  
Code:
  t = int(input())
  for i in range(t):
      n = list(map(int,input().split()))
      n.remove(max(n))
      print(max(n))
      
# This is the solution for this problem. This is one of the most simplest solution for this problem.
# We can solve this problem by using loops also but here I used this simplest method. This is a very 
# beginner friendly question.
# if you like the code;
#   Give a star
# else:
#   Give a star
