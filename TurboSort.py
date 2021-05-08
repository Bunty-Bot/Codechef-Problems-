# Question:
#   Given the list of numbers, you are to sort them in non decreasing order.
# Input:
#   t – the number of numbers in list, then t lines follow [t <= 10^6]. 
#   Each line contains one integer: N [0 <= N <= 10^6]
# Output:
#   Output given numbers in non decreasing order.
# Example:
#   Input:

#   5
#   5
#   3
#   6
#   7
#   1
#   Output:

#   1
#   3
#   5
#   6
#   7
  
# Code:
  
t = int(input())
li=[]
for i in range(t):
    n = int(input())
    li.append(n)
li.sort()
for j in li:
    print(j)
  
# This is the solution for the Turbo Sort problem. This is the 9th problem in the beginner's section.
# You can have multiple ways of solving it. You can solve it by Recursion or by Iteration.
# If you like the code:
#   Give a star.
# else:
#   Give a star.
