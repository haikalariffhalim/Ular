def sum_of_diff(games):
    games.sort(reverse=True)
    sum = 0
    for i in range(len(games) - 1):
        sum += games[i] - games[i + 1]
    return sum
