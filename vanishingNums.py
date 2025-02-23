sortedList,k=list(map(int,input().strip().split(","))),int(input())
Naturals = {i for i in range(1,max(sortedList)+k+1)}
missings = sorted(Naturals.difference(set(sortedList)))
print(missings[k-1])