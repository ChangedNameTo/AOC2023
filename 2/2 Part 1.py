limits_dict = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('input.txt') as file:
    # with open('sample.txt') as file:
    total = 0
    for line in file:

        game_split_line = line.strip().split(': ')
        game_number = game_split_line[0].split(' ')[1]

        pulls_split_line = game_split_line[1].split('; ')

        invalid_game = False

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

                if counts_dict[color] > limits_dict[color]:
                    invalid_game = True
                    break

            if invalid_game:
                break

        if not invalid_game:
            total += int(game_number)

    print(total)
