import re
import numpy as np

# Part 1
df = [list(line) for line in open('data.txt').read().splitlines()]
matrix = np.array(df)

diags = [''.join(np.diagonal(matrix, offset=i).tolist()) for i in range(-139, 140)]
diags.extend([''.join(np.fliplr(matrix).diagonal(offset=i).tolist()) for i in range(-139, 140)])

lines = open('data.txt').read().splitlines()
cols = [''.join(matrix[:, c].tolist()) for c in range(matrix.shape[1])]

a = diags + lines + cols

n = 0
for i in a:
    x = len(re.findall(r'(?=(XMAS|SAMX))', i))
    n += x

print(f'Part 1 Answer: {n}')

n = 0

gx, gy = matrix.shape
for i in range(gx - 3 + 1):
    for j in range(gy - 3 + 1):
        subgrid = matrix[i:i + 3, j:j + 3]
        x = ''.join(np.diagonal(subgrid))
        y = ''.join(np.fliplr(subgrid).diagonal())
        if len(re.findall(r'SAM|MAS', x)) & len(re.findall(r'SAM|MAS', y)) > 0:
            n += 1

print(f'Part 2 Answer: {n}')