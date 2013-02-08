import re

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']


def number_to_english(number):
    '''Convert a number from 1 to 1000 to it's engish representation'''
    if number == 1000:
        return 'one-thousand'

    output = ''
    num_str = str(number)

    if number >= 100:
        hundred_digit = int(num_str[0])
        output = '{0}-hundred'.format(ones[hundred_digit])
        num_str = num_str[1::]
        number = int(num_str)

    if number > 0:
        join = ' and ' if len(output) > 0 else ''
        output += '{0}{1}'.format(join, convert_less_than_one_hundred(number))

    return output


def convert_less_than_one_hundred(number):
    num_str = str(number)
    output = ''
    if number >= 20:
        tens_didget = int(num_str[0])
        output += tens[tens_didget]
        number_digit = int(num_str[1])
        if number_digit != 0:
            output += '-{0}'.format(ones[number_digit])

    if number < 20:
        output += ones[number]
    return output


def euler_problem17():
    total = 0
    for number in range(1, 1001):
        string_rep = re.sub(r'[\s-]', '', number_to_english(number))
        total += len(string_rep)
    return total


if __name__ == "__main__":
    print euler_problem17()
