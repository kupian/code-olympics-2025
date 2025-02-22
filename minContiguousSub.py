from itertools import permutations

s,t=input(),input()


tPermutations = set("".join(p) for p in permutations(t))

indexes = []

for perm in tPermutations:
    i = s.find(perm)
    if i >= 0:
        indexes.append(i)

if indexes==[]:
    print("")
else:
    minIndex = min(indexes)
    print(s[minIndex:minIndex+len(perm)])


