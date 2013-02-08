convert = {
    4: ['', 'M', 'MM', 'MMM'],
    3: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    2: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    1: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
}


def number_to_numeral_iterative(number):
    numeral = ''
    number_as_string = str(number)
    for idx, digit in enumerate(number_as_string):
        magnitude = len(number_as_string) - idx
        numeral += convert[magnitude][int(digit)]
    return numeral


def number_to_numeral_rec(number):
    number_as_string = str(number)
    if len(number_as_string) == 0:
        return ''
    digit = number_as_string[0]
    numeral = convert[len(number_as_string)][int(digit)]
    return numeral + number_to_numeral_rec(number_as_string[1:])


letter_magnitude = {
    'I': 1,
    'V': 1,
    'X': 2,
    'L': 2,
    'C': 3,
    'D': 3,
    'M': 4,
}


def numeral_to_number(numeral):
    if len(numeral) == 0:
        return ''

    number_as_string = ''
    buff = ''
    current_magnitude = letter_magnitude[numeral[0]]

    def convert_numeral_buffer():
        digit = str(convert[current_magnitude].index(buff))
        digit += '0' * (current_magnitude - digit_magnitude - 1)
        return digit

    for letter in numeral.upper():
        digit_magnitude = letter_magnitude[letter]
        if digit_magnitude < current_magnitude:
            number_as_string += convert_numeral_buffer()
            current_magnitude = digit_magnitude
            buff = letter
        else:
            buff += letter
    digit_magnitude = 0
    number_as_string += convert_numeral_buffer()
    return int(number_as_string)
