n = int(input())
dp = [0]
for i in range(1, n+1):
    if i == 1:
        dp.append(1)
    elif i == 2:
        dp.append(3)
    else:
        dp.append(dp[i-1] + 2 * dp[i-2])
print(dp[-1] % 10007)
