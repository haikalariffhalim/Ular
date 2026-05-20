def points(games):
    points = 0

    for game in games:
        if game[0] > game[2]:
            points += 3
        elif game[0] == game[2]:
            points += 1
        else:
            points += 0

    return points


print(f"Your score is {points([])}")
