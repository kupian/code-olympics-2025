M,N,stringM,stringN = int(input()),int(input()),input(),input()


memo  = {}

def counter(i,j):
    if i>=M or j>=N:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    

    if stringM[i] == stringN[j]:
        memo[(i,j)] = counter(i+1,j+1)+1
        return memo[(i,j)]

    memo[(i,j)]=0
    return 0

maxCount = 0
for i in range(M):
    for j in range(N):
        maxCount = max(maxCount, counter(i,j))


print(maxCount)


#thank you john williamson i finally found a use for memoization