import re

DIGITS = '0123456789'
SPACES = '.'
DATA = '.0123456789'


def array_clamp(value, array):
    return max(0, min(value, len(array)-1))


# with open('sample.txt') as file:
with open('input.txt') as file:
    array2d = list(map(lambda line: list(line.strip()), file.readlines()))

    y_counter = 0
    valid_numbers = []
    for line in array2d:
        x_counter = 0

        found_number = []
        starting_x = None
        ending_x = None
        isValid = False

        for character in line:
            if character in DIGITS:
                found_number.append(character)

                if starting_x is None:
                    starting_x = x_counter
            if (character in DIGITS and x_counter == len(line)-1) or starting_x is not None:
                found_number = int(''.join(found_number))
                ending_x = x_counter - 1

                # Check for validity
                for y in range(y_counter-1, y_counter+2):
                    for x in range(starting_x-1, ending_x+2):
                        x = array_clamp(x, line)
                        y = array_clamp(y, array2d)
                        if array2d[y][x] not in DATA:
                            isValid = True
                            break
                    if isValid:
                        # print('appending')
                        valid_numbers.append(found_number)
                        break

                ending_x = None
                starting_x = None
                found_number = []
                isValid = False

            x_counter += 1
        y_counter += 1

board = list(open('input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
         if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

sol = [p for q in chars.values() for p in q]

print([item for item in valid_numbers if item not in sol])
print([item for item in sol if item not in valid_numbers])
