import random
new = ["pakistan","india","bangledash","srilanka","newzeland","australia","africa","afganistan","westendise"]
time1 = ["Sun - 10:00","Mun - 10:00","Tus - 10:00","Wen - 10:00","Thes - 10:00","Fri - 10:00"]
def game():
        time = random.choice(time1)
        team1 = random.choice(new)
        team2 = random.choice(new)
        if team1 == team2:
            return
        else:
            new1 = f'{i} =  {time} \ {team1}  "VS"  {team2}\n'
            print(new1)
        with open("11_match_cricket.txt","a")as f:
             f.write(str(new1))
for i in range(1,31):
     game()
