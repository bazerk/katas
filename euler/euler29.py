

def euler_problem29(max):
    uniques = set()
    for a in range(2, max + 1):
        for b in range(2, max + 1):
            uniques.add(a ** b)
    return len(uniques)

if __name__ == '__main__':
    print euler_problem29(100)
