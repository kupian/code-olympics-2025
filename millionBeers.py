N, B = int(input()),input().split()

B = [int(b) for b in B]


million = 1000000

pubCount = 0

for pub in B:

    million -= pub
    if million < 0:
        million += pub
    else:
        pubCount += 1

print(pubCount)
