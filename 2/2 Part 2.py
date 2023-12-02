import functools

with open('input.txt') as file:
    # with open('sample.txt') as file:
    total = 0
    for line in file:
        game_split_line = line.strip().split(': ')
        game_number = game_split_line[0].split(' ')[1]

        pulls_split_line = game_split_line[1].split('; ')

        min_dict = {}

        for game_pulls in pulls_split_line:
            counts_dict = {}

            for individual_pulls in game_pulls.split(', '):
                individual_pulls_split = individual_pulls.split(' ')
                count = individual_pulls_split[0]
                color = individual_pulls_split[1]

                if color not in counts_dict:
                    counts_dict[color] = int(count)
                else:
                    counts_dict[color] += int(count)

            for color in counts_dict:
                if color not in min_dict:
                    min_dict[color] = counts_dict[color]
                else:
                    min_dict[color] = max(min_dict[color], counts_dict[color])

        game_power = functools.reduce(lambda a, b: a*b, min_dict.values())
        total += game_power

    print(total)
