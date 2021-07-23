# Question:-
#   Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
#   If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.
  
# Input:-
#   The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
  
# Output:-
#   For each test case, display the smallest number of notes that will combine to give N, in a new line.
  
# Constraints:-
#   1 ≤ T ≤ 1000
#   1 ≤ N ≤ 1000000
  
# Example:-
#   Input
#   3 
#   1200
#   500
#   242

#   Output
#   12
#   5
#   7
  
Code:- 
  t = int(input())
  for i in range(t):
      n=int(input())
      c=0
      while(n>0):
          if(n>=100):
              c+=1
              n=n-100
          elif(n>=50):
              c+=1
              n=n-50
          elif(n>=10):
              c+=1    
              n=n-10
          elif(n>=5):
              c+=1
              n=n-5
          elif(n>=2):
              c+=1
              n=n-2
          else:
              c+=1
              n=n-1

      print(c)
      
# This was a little bit tricky but if you understand the concept then you will find this easy. You have to think very carefully for this problem.
# What is asked and what we are going to do is very important in this type of problem.
# if you like the code:
#   give a star
#  else:
#   give a star
