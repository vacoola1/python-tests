screen1 = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

screen = screen1

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


def display_screen():
    for row in screen:
        for symbol in row:
            print(symbol, end='')
            print(' ', end='')
        print()


def active_blocks():
    raw_blocks = {}
    for symbol in payout:
        positions = []
        for asix, row in enumerate(screen):
            for asiy, sym in enumerate(row):
                if sym == symbol:
                    positions.append({'x': asix, 'y': asiy})
        if len(positions) > 0:
            raw_blocks[symbol] = positions

    for symbol, positions in raw_blocks.items():
        blocks = []
        positions_copy = list(positions)

        blocks.append([positions_copy[0]])
        positions_copy.remove(positions_copy[0])

        has_positions = len(positions_copy) > 0

        while has_positions:
            for block in blocks:
                for pos_in_block in list(block):
                    for pos in list(positions_copy):
                        if pos['x'] == pos_in_block['x'] | pos['y'] == pos_in_block['y']:
                            block.append(pos)
                            positions_copy.remove(pos)
            has_positions = len(positions_copy) > 0


# 1 2 2 4 5 6
# 1 2 3 4 5 6
# 1 3 3 3 5 6
# 1 2 3 4 5 6
# 1 2 2 4 5 6

display_screen()
active_blocks()
