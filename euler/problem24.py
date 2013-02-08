

def generate_lexigraphocial(sequence):
    if len(sequence) == 1:
        yield sequence
        return

    for item in sequence:
        subsequence = filter(lambda x: x != item, sequence)
        for output in generate_lexigraphocial(subsequence):
            yield [item] + output


def euler_problem24(sequence):
    count = 0
    for item in generate_lexigraphocial(sequence):
        count += 1
        if count == 1000000:
            return item
    return None


if __name__ == '__main__':
    print euler_problem24([x for x in '0123456789'])
