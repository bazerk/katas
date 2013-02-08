import euler


def euler_problem21():
    set_of_amicable = set()
    for i in range(10000):
        test_for_amicability(i, set_of_amicable)
    print set_of_amicable
    return sum(set_of_amicable)


def test_for_amicability(number, set_of_amicable):
    if number in set_of_amicable:
        return
    test_pair = sum(euler.iterator_divisors(number))
    if test_pair in set_of_amicable or test_pair == number:
        return
    test_number = sum(euler.iterator_divisors(test_pair))
    if test_number == number:
        set_of_amicable.add(number)
        set_of_amicable.add(test_pair)

if __name__ == "__main__":
    print euler_problem21()
