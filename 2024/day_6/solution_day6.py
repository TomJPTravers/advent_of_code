def load_data(d):
    area = {}
    for y, line in enumerate(reversed(d.splitlines())):
        for x, p in enumerate(line):
            if p in ['^', '>', 'v', '<']:
                position = (x, y)
                symb = p
            area[x, y] = p

    return position, symb, area


N = (0, 1)
E = (1, 0)
S = (0, -1)
W = (-1, 0)

direction = {'^': N, '>': E, 'v': S, '<': W}
turn = {N: E, E: S, S: W, W: N}

# Part 1
df = open('data.txt').read()
position, symbol, lab = load_data(df)
start = position

heading = direction[symbol]
visited = {position}
while tuple(map(lambda i, j: i + j, position, heading)) in lab:
    if lab[tuple(map(lambda i, j: i + j, position, heading))] == '#':
        heading = turn[heading]
    else:
        position = tuple(map(lambda i, j: i + j, position, heading))
        visited.add(position)

print(f'Guard visited {len(visited)} squares')

# Part 2
visited.remove(start)
n = 0

for v in visited:
    lab_2 = lab.copy()
    lab_2[v] = '#'
    heading = direction[symbol]
    position = start
    visited_2 = []

    loop = False
    while tuple(map(lambda i, j: i + j, position, heading)) in lab_2:
        next_pos = tuple(map(lambda i, j: i + j, position, heading))

        if lab_2[next_pos] == '#':
            heading = turn[heading]
        else:
            if position in visited_2:
                index = visited_2.index(position)
                if index + 1 < len(visited_2) and visited_2[index + 1] == next_pos:
                    print(f" Loop detected!")
                    loop = True
                    break
            position = next_pos
            visited_2.append(position)

    if loop:
        n += 1

print(f"Total positions causing loops: {n}")