import itertools
from collections import defaultdict
from fractions import Fraction

data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def load_data(d):
    area = []
    tower = defaultdict(list)
    t = [i for i in list(set(d)) if i not in {".", "\n"}]
    for y, line in enumerate(d.splitlines()):
        for x, p in enumerate(line):
            if p in t:
                tower[p].append((x, y))
            area.append((x, y))

    return area, dict(tower)


def where_antinodes(points):
    nodes = []
    while len(points) > 1:
        x1, y1 = points[0]
        for x2, y2 in points[1:]:
            dx = x2 - x1
            dy = y2 - y1
            nodes.append((x1 - dx, y1 - dy))
            nodes.append((x2 + dx, y2 + dy))
        points.pop(0)
    return nodes


# Part 1
area, towers = load_data(open("data.txt").read())
all_antinodes = set()  # Create a set to store unique antinode coordinates
for a, b in towers.items():
    # Get the list of antinodes and add them to the set
    antinodes = where_antinodes(b)
    all_antinodes.update(antinodes)  # Add the antinodes to the set

print(f"Numer of Anti-nodes is {sum(i in set(area) for i in list(all_antinodes))}")

# Part 2


def where_antinodes_pt2(p1, p2, max_x, max_y):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        for y in range(0, max_y + 1):
            yield (x1, y)
    else:
        dx = x2 - x1
        dy = y2 - y1
        for x in range(0, max_x + 1):
            d = Fraction(x1 - x, dx) * dy
            if d.denominator == 1:
                y = y1 - d.numerator
                if 0 <= y <= max_y:
                    yield (x, y)


area, towers = load_data(open("data.txt").read())
all_antinodes = set()
max_x = max(p[0] for p in area)
max_y = max(p[1] for p in area)
for t in towers:
    for p1, p2 in itertools.combinations(towers[t], r=2):
        all_antinodes |= set(where_antinodes_pt2(p1, p2, max_x, max_y))

print(f"Numer of Anti-nodes is {len(all_antinodes)}")

# test comment
