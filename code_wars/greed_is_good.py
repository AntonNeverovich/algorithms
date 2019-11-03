def score(dice):
    results = get_results(dice)
    return ((results.get(1) // 3) * 1000 + (results.get(1) % 3) * 100
           + results.get(5) // 3 * 500 + results.get(5) % 3 *50
           + results.get(6) // 3 * 600
           + results.get(4) // 3 * 400
           + results.get(3) // 3 * 300
           + results.get(2) // 3 * 200)


def count_dice(x: int, dice: list):
    count = 0
    for d in dice:
        if x == d:
            count += 1
    return count


def get_results(dice: list):
    keys = list(range(1, 7))
    values = [count_dice(d, dice) for d in keys]
    return dict(zip(keys, values))
