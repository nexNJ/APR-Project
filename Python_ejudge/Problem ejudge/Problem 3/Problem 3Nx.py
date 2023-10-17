team = int(input())
players = int(input())
count_player = 0
count_team_score = 0

while count_player < team*players:
  x = int(input())
  count_player +=1
  if count_player % players ==1:
    min = x
  elif x < min:
    min = x
  if count_player % players ==0:
    if count_team_score ==0:
      team_score = min
      min =0
      count_team_score +=1
      win = count_player // players

    else:
        if min > team_score:
            team_score = min
            min = 0
            count_team_score +=1
            win = count_player // players
        else:
           count_team_score +=1
 

print(f'Team {win}')