import pprint

screen = [[1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6]]


WILD = 2

payout = {
    1: {
        1: 0,
        2: 20
    },
    2: {
        1: 0,
    },
    3: {
        1: 0,
        2: 20,
        3: 30
    },
    4: {
        1: 0,
        2: 20,
        3: 30
    },
    5: {
        1: 0,
        2: 20,
        3: 30
    },
    6: {
        1: 0,
        2: 20,
        3: 30
    },
    7: {
        1: 0,
        2: 20,
        3: 30
    },
    8: {
        1: 0,
        2: 20,
        3: 30
    }
}


def symbol_payout(symbol, count):
    pay = 0
    if symbol in payout:
        for s_count, s_pay in payout[symbol].items():
            if count >= s_count & pay < s_pay:
                pay = s_pay
    return pay


def find_symbols_positions():
    symbols_positions = {}
    for symbol in payout:
        positions = []
        for x, row in enumerate(screen):
            for y, screen_symbol in enumerate(row):
                if screen_symbol == symbol:
                    positions.append({'x': x, 'y': y})

        if len(positions) > 0:
            symbols_positions[symbol] = positions

    return symbols_positions


def find_symbols_blocks():
    raw_blocks = find_symbols_positions()
    blocks = {}
    for symbol, positions in raw_blocks.items():
        blocks[symbol] = group(positions)

    return blocks


def group(positions):
    if len(positions) == 0:
        return {}

    positions_copy = list(positions)

    blocks = []
    while len(positions_copy) > 0:

        new_block = [positions_copy[0]]
        positions_copy.pop(0)

        has_stack = True
        while has_stack:
            has_stack = False
            for pos_in_block in list(new_block):
                for pos in list(positions_copy):
                    if stacked(pos_in_block, pos):
                        new_block.append(pos)
                        positions_copy.remove(pos)
                        has_stack = True

        blocks.append(new_block)

    return blocks


def stacked(position1, position2):
    return (position1['x'] == (position2['x'] + 1) & position1['y'] == position2['y']) | \
           ((position1['x'] + 1) == position2['x'] & position1['y'] == position2['y']) | \
           (position1['x'] == position2['x'] & position1['y'] == (position2['y'] + 1)) | \
           (position1['x'] == position2['x'] & (position1['y'] + 1) == position2['y'])


def display_screen():
    print(' *** screen ***')
    print()
    pprint.pprint(screen)
    print()


def display_blocks(blocks):
    print(' *** blocks ***')
    print()
    pprint.pprint(blocks)
    print()


# 1 2 2 4 5 6
# 1 2 3 4 5 6
# 1 3 3 3 5 6
# 1 2 3 4 5 6
# 1 2 2 4 5 6


display_screen()
display_blocks(find_symbols_blocks())
