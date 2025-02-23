M,N,stringM,stringN = int(input()),int(input()),input(),input()

dp = [[0] * (N + 1) for _ in range(M + 1)]
maxCount = 0

for i in range(1, M + 1): 
    for j in range(1, N + 1):
        if stringM[i - 1] == stringN[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            maxCount = max(maxCount, dp[i][j]) 

print(maxCount)