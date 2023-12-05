from collections import defaultdict


# cards = list(open('sample.txt'))
cards = list(open('input.txt'))

total = 0
cards_dict = defaultdict(int)

for idx, x in enumerate(cards):
    cards_dict[idx] += 1
    first, last = x.strip().split('|')
    winning_numbers = [int(x) for x in first.split(':')[1].split()]
    my_numbers = [int(x) for x in last.split()]
    winners = len(set(my_numbers) & set(winning_numbers))

    for j in range(winners):
        cards_dict[idx + j + 1] += cards_dict[idx]

    print(cards_dict)
print(sum(cards_dict.values()))
