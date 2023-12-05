# cards = list(open('sample.txt'))
cards = list(open('input.txt'))

total = 0
for card in cards:
    first, last = card.strip().split('|')
    winning_numbers = [int(x) for x in first.split(':')[1].split()]
    my_numbers = [int(x) for x in last.split()]
    winners = len(set(my_numbers) & set(winning_numbers))
    if winners > 0:
        total += 2**(winners-1)

print(total)
