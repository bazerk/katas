TARGET = 200
DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]
seen = {}


def find_solutions(target, max_coin=None):
    if target == 0:
        return
    if max_coin is None:
        max_coin = 200
    for coin in DENOMINATIONS:
        if coin > max_coin:
            continue
        if coin <= target:
            solution = [coin]
            new_target = target - coin
            if new_target:
                for x in find_solutions(target - coin, coin):
                    yield solution + x
            else:
                yield solution


def find_solution_count(target, max_coin=None):
    if target == 0:
        return 1
    if max_coin is None:
        max_coin = 200
    key = '%d_%d' % (target, max_coin)
    if key in seen:
        return seen[key]
    count = 0
    for coin in DENOMINATIONS:
        if coin > max_coin:
            continue
        if coin <= target:
            count += find_solution_count(target - coin, coin)
    seen[key] = count
    return count


def problem31():
    # for x in find_solutions(10):
    #     print x
    return find_solution_count(200)


if __name__ == '__main__':
    print problem31()
