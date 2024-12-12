r, p = open('data.txt').read().split('\n\n')

rules = []
for l in r.splitlines():
    a,b = l.split('|')
    rules.append((int(a),int(b)))

update = []
for l in p.splitlines():
    x = [int(a) for a in l.split(',')]
    update.append(x)

def find_middle(x):
    return x[len(x) // 2]


# Part 1
valid_updates = []
non_valid_updates = []
for i in update:
    good = True
    for j in i:
        after = [a[1] for a in rules if a[0] == j]
        before = [a[0] for a in rules if a[1] == j]

        bad_before = [a for a in i[i.index(j) + 1:] if a in before]
        bad_after = [a for a in i[:i.index(j)] if a in after]
        if len(bad_before) or len(bad_after) > 0:
            good = False

    if good:
        valid_updates.append(i)
    else:
        non_valid_updates.append(i)

print(sum(find_middle(x) for x in valid_updates))


# Part 2
def bubble_sort(nums, rules):
    n = len(nums)
    rule_set = set(rules)

    for i in range(n):
        for j in range(n - 1):
            if (nums[j], nums[j + 1]) in rule_set:
                continue
            elif (nums[j + 1], nums[j]) in rule_set:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

x = [bubble_sort(i, rules) for i in non_valid_updates]
print(sum(find_middle(i) for i in x))