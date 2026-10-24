justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print("Justice league at first:", justice_league)
print(f"\n1. Number of members: {len(justice_league)}")

justice_league.extend(["Batgirl","Nightwing"])
print(f"\n2. New list: {justice_league}")

justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print(f"\n3. Wonder Woman is now leader and the league is now:",justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash") + 1,"Superman")
print(f"\n4. Separated Aquaman and Flash by Superman and the league is now:",justice_league)

justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunetr","Green Arrow"]
print("\n5. New justice league: ", justice_league)

justice_league.sort()
print("\n6. Alphabetically sorted justice league: ", justice_league)
print("New Leader is:", justice_league[0])