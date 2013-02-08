import sys


def main():
    word_set = set()
    with open('../dictionary.txt') as f:
        for word in f.read().split():
            word_set.add(word)

    input_letters = ''.join(sys.argv[1::])
    print input_letters


if __name__ == '__main__':
    main()
