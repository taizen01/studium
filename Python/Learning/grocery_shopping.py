team1 = ["Yoda"]
team2= ["Jack","Rose"]
team3= ["Vader", "Leah"]

frage = input("Welches Team wählst du? [Team1, Team2, Team3]\n")


match frage:
    case "team1":
        print("good")
        count = len(team1)
    case "team2":
        print("good")
        count = len(team2)
    case "team3":
        print("not good")
        count = len(team3)


if (count%2) == 0:
    print("Gerade Anzahl an Teammitgliedern")
else:
    print("Ungerade Anzahl an Teammitgliedern")
