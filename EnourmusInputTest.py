# Question:-
#   The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems 
#   branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.
  
# Input:-
#   The input begins with two positive integers n k (n, k<=107). The next n lines of 
#   input contain one positive integer ti, not greater than 109, each.
  
# Output:-
#   Write a single integer to output, denoting how many integers ti are divisible by k.
  
# Example:-
#   Input:
# 7 3
# 1
# 51
# 966369
# 7
# 9
# 999996
# 11

# Output:
# 4

Code:-
  str = input().split()
n = int(str[0])
k = int(str[1])
ans = 0

for i in range(n):
    a = int(input())
    if a%k==0:
        ans = ans + 1
print(ans)

#This is the code for Enourmus Input Test. This is the second problem in Beginner's Section.
#Thank you for reading my code!!!
#if you like:
#   give a star
#else:
#   give a star
