import pprint

SCREEN = [[1, 1, 1, 4, 5, 6, 7],
          [1, 2, 3, 4, 5, 6, 7],
          [1, 2, 3, 4, 5, 6, 6],
          [1, 1, 6, 1, 5, 6, 6],
          [1, 2, 3, 1, 8, 8, 7],
          [1, 2, 3, 4, 8, 8, 7]]


WILD = 2

PAYOUT_SINGLE = {
    1: {
        1: 0,
        2: 20
    }
}

PAYOUT = {
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


def symbol_payout(symbol, count, payout):
    pay = 0
    if symbol in payout:
        for s_count, s_pay in payout[symbol].items():
            if count >= s_count & pay < s_pay:
                pay = s_pay
    return pay


def find_symbols_positions(payout, screen, wild):
    symbols_positions = {}
    for symbol in payout:
        positions = []
        for x, row in enumerate(screen):
            for y, screen_symbol in enumerate(row):
                if screen_symbol == symbol or screen_symbol == wild:
                    positions.append({'x': x, 'y': y})

        if len(positions) > 0:
            symbols_positions[symbol] = positions

    return symbols_positions


def find_symbols_blocks(symbols_positions):
    blocks = {}
    for symbol, positions in symbols_positions.items():
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


def stacked(pos1, pos2):
    return (pos1['x'] == pos2['x'] + 1 and pos1['y'] == pos2['y']) or \
           (pos1['x'] + 1 == pos2['x'] and pos1['y'] == pos2['y']) or \
           (pos1['x'] == pos2['x'] and pos1['y'] == pos2['y'] + 1) or \
           (pos1['x'] == pos2['x'] and pos1['y'] + 1 == pos2['y'])


def display(title, screen):
    print(' *** ' + title + ' ***')
    print()
    pprint.pprint(screen)
    print()


def run():
    positions = find_symbols_positions(PAYOUT, SCREEN, WILD)
    blocks = find_symbols_blocks(positions)

    display("screen", SCREEN)
    display("positions", positions)
    display("blocks", blocks)


run()
