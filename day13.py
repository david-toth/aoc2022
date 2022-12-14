from functools import cmp_to_key

with open("inputs/day13.txt") as f:
	data = f.read().strip()

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int):
		if left < right:
			return -1
		elif left == right:
			return 0
		else:
			return 1
	elif isinstance(left, list) and isinstance(right, list):
		i = 0
		while i < len(left) and i < len(right):
			result = compare(left[i], right[i])
			if result == -1 or result == 1:
				return result
			i += 1
		if i == len(left) and i < len(right):
			return -1
		elif i < len(left) and i == len(right):
			return 1
		else:
			return 0
	elif isinstance(left, int) and isinstance(right, list):
		return compare([left], right)
	else:
		return compare(left, [right])

ordered = []
sum_indices = 0
for i, lr in enumerate(data.split('\n\n')):
	left, right = lr.split('\n')
	left = eval(left)
	right = eval(right)
	ordered.append(left)
	ordered.append(right)
	if compare(left, right) == -1:
		sum_indices += (i + 1)
print(sum_indices)

ordered.append([[2]])
ordered.append([[6]])
ordered = sorted(ordered, key=cmp_to_key(lambda l, r: compare(l, r)))
part2 = 1
for i, x in enumerate(ordered):
	if x == [[2]] or x == [[6]]:
		part2 *= (i+1)
print(part2)