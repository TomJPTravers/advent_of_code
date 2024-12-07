import re

df = open('data.txt').read()

def calc_mul(text):
    muls = re.findall(r'mul\((\d{1,3}),\s?(\d{1,3})\)', text)
    digits = [list(map(int, i)) for i in muls]
    n = sum(a * b for a, b in digits)

    return n

# Part 1
n = calc_mul(df)
print(f'Part 1 Answer:  {n}')

# Part 2
split_text = re.split(r"(don't\(\)|do\(\))", df)
text = split_text[0::2]
instructions = split_text[1::2]
instructions.insert(0, 'do()')
keep = [text[i] for i, j in enumerate(instructions) if j == 'do()']

n = calc_mul(''.join(text))
print(f'Part 2 Answer:  {n}')