M,N,stringM,stringN = int(input()),int(input()),input(),input()

def counter(i,j,count):
    if i>=M or j>=N or (stringM[i] != stringN[j]):
        return count
    return counter(i+1,j+1,count+1)

maxCount = 0
for i in range(M):
    for j in range(N):
        maxCount = max(maxCount, counter(i,j,0))

        
print(maxCount)
