

def euler_problem9():
    for a in range(1, 997):
        for b in range(1, (1000 - a)):
            c = 1000 - a - b
            if (a ** 2 + b ** 2) == (c ** 2):
                return a * b * c
    return None

if __name__ == "__main__":
    print euler_problem9()
