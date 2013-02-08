

def get_alphabet_map():
    a_val = ord('A')
    vals = {}
    for i in range(26):
        char = chr(a_val + i)
        vals[char] = i + 1
    return vals


def euler_problem22():
    alphabet_map = get_alphabet_map()
    with file('names.txt', 'r') as f:
        names_content = f.read()
    names = [name.replace('"', '') for name in names_content.split(',')]
    total = 0
    for idx, name in enumerate(sorted(names)):
        name_sum = sum(alphabet_map[x] for x in name)
        total += name_sum * (idx + 1)
    return total

if __name__ == '__main__':
    print euler_problem22()
