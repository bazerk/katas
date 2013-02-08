import re


def convert(inputString):
    def consider_upper(ch):
        return ch.isupper() or ch.isdigit()

    inputString = re.sub(r'-|_', ' ', inputString)
    inputString = inputString.strip()

    output = ''
    prev_upper = True
    prev_whitespace = True
    last_index = len(inputString) - 1

    for ix, ch in enumerate(inputString):
        if prev_whitespace:
            ch = ch.upper()
        current_upper = consider_upper(ch)
        current_whitespace = ch.isspace()
        if current_upper and not prev_whitespace:
            if not prev_upper:
                output = output + ' '
            elif ix < last_index and not consider_upper(inputString[ix + 1]):
                output = output + ' '
        output = output + ' ' if current_whitespace else output + ch
        prev_upper = current_upper
        prev_whitespace = current_whitespace
    return output
