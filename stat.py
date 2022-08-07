import requests
import matplotlib.pyplot as plt

startYear = 1990
lastYear = 2021

home = []
visit = []
for item in range(startYear, lastYear):
    h=0
    v=0
    resp = requests.get(f"https://www.balldontlie.io/api/v1/games?seasons[]={item}").json()
    for x in resp["data"]:
        if x["home_team_score"] > x["visitor_team_score"]:
            h+=1
        elif x["home_team_score"] < x["visitor_team_score"]:   
            v+=1
    home.append(h)
    visit.append(v)

fig, ax = plt.subplots(2)
ax[0].plot(range(1990, 2021), home, label='home team total wins')
ax[0].plot(range(1990, 2021), visit, label='visitor team total wins')
ax[0].legend()
ax[1].pie([sum(home)/(sum(home)+sum(visit))*100, sum(visit)/(sum(home)+sum(visit))*100], labels = [f"Home games: {sum(home)}", f"Visit games: {sum(visit)}"], autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
