

alien_color = input("green or yellow or red: ")
points = 0

if alien_color == "green":
    print("player earned 5 points")
    points += 5
else:
    print("player did not score points")

print("points: ", points)