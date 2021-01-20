arr = [10, 20, 20, 10, 10, 30]
no_of_pairs = 0
spare = []

for i in arr:
    if i in spare:
        spare.remove(i)
        no_of_pairs += 1
    else:
        spare.append(i)
print(no_of_pairs)
