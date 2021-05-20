# Question:
#   The game of billiards involves two players knocking 3 balls around on a green baize table. Well, there is more to it, but for our purposes this is sufficient.
#   The game consists of several rounds and in each round both players obtain a score, based on how well they played. Once all the rounds have been played, the total 
#   score of each player is determined by adding up the scores in all the rounds and the player with the higher total score is declared the winner.
#   The Siruseri Sports Club organises an annual billiards game where the top two players of Siruseri play against each other. The Manager of Siruseri Sports Club 
#   decided to add his own twist to the game by changing the rules for determining the winner. In his version, at the end of each round, the cumulative score for each 
#   player is calculated, and the leader and her current lead are found. Once all the rounds are over the player who had the maximum lead at the end of any round in the 
#   game is declared the winner. Your task is to help the Manager find the winner and the winning lead. You may assume that the scores will be such that there will always 
#   be a single winner. That is, there are no ties.
  
# Input:
#   The first line of the input will contain a single integer N (N ≤ 10000) indicating the number of rounds in the game. Lines 2,3,...,N+1 describe the scores of the 
#   two players in the N rounds. Line i+1 contains two integer Si and Ti, the scores of the Player 1 and 2 respectively, in round i. You may assume that 1 ≤ Si ≤ 1000 
#   and 1 ≤ Ti ≤ 1000.
  
# Output:
#   Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and indicates the winner and L is the maximum lead attained by the 
#   winner.
  
# Example:
#   Input:
#   5
#   140 82
#   89 134
#   90 110
#   112 106
#   88 90
#   Output:
#   1 58
  
# Code:
  d={1:0,2:0}
  c1=0
  c2=0
  for _ in range(int(input())):
      p1,p2=map(int,input().split())
      c1+=p1
      c2+=p2
      if c1>c2:
          d[1]=max(d[1],c1-c2)
      else:
          d[2]=max(d[2],c2-c1)
  if d[1]>d[2]:
      print(1,d[1])
  else:
      print(2,d[2])
      
# This is the code for the lead game problem. This was a slightly tough problem for beginners.
# This problem tests many skills of the programmer as it has aspects of different programming topics.
# if you like the code:
#   Give a star.
# else:
#   Give a star.
