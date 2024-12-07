# load data
l = []
r = []
for x, y in [l.split() for l in open('input.txt').read().splitlines()]:
    l.append(int(x))
    r.append(int(y))

# Part 1
x = zip(sorted(l), sorted(r))
diff = sum(abs(z-y) for z,y in x)
print(f'Part 1 Answer: {diff}')

# Part 2
sim_score = sum(x*r.count(x) for x in l)
print(f'Part 2 Answer: {sim_score}')