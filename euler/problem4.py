

def euler_problem4():
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            res = i * j
            if check_number_is_palindrome(res) and largest < res:
                largest = res
    return largest


def check_number_is_palindrome(number):
    numstr = str(number)
    for i in range(0, len(numstr) / 2):
        if numstr[i] != numstr[-(1 + i)]:
            return False
    return True
