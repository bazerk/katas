

def euler_problem2(limit):
    return sum([x for x in fibbonaci(limit) if x % 2 == 0])


def fibbonaci(limit):
    prev = 1
    current = 1
    while current < limit:
        yield current
        current = current + prev
        prev = current - prev
