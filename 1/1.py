import os
import functools
import re

# input = '1.txt'
input = 'test.txt'

number_mapping = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def convert_to_digit(matched_number):
    if (matched_number.isdigit()):
        return matched_number
    else:
        return str(number_mapping[matched_number])


with open(input) as f:
    sums = []
    for line in f:

        pattern = re.compile(
            r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))')

        # Test the regex
        matches = pattern.findall(line)
        first = convert_to_digit(matches[0])
        last = convert_to_digit(matches[-1])
        sums.append(first + last)

    total = functools.reduce(lambda x, y: int(x) + int(y), sums)

    print(total)
