# load data
df = [list(map(int, l.split())) for l in open("input2.txt").read().splitlines()]

# Part 1
def check_safety(line):
    line_pairs = [(i,j) for i,j in zip(line, line[1:])]
    increasing = [i < j for i,j in line_pairs]
    decreasing = [i > j for i,j in line_pairs]
    in_tolerance = [1 <= abs(i-j) <= 3 for i,j in line_pairs]

    return (all(increasing) or all(decreasing)) and all(in_tolerance)

safe = sum(check_safety(line) for line in df)
print(f'Part 1 Answer: {safe}')

# Part 2
def safety_fix(line):
    passes = 0
    for i in range(len(line)):
        subline = line[0:i] + line[i+1:]
        if check_safety(subline):
            passes += 1
    return passes > 0

fails = [line for line in df if not check_safety(line)]

# part 2
new_safe = sum(safety_fix(line) for line in fails) + safe
print(f'Part 2 Answer: {new_safe}')