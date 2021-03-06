# 틀림
# N = int(input())
# res = 0
# while N:
#     N -= (int(N**0.5))**2
#     res += 1
# print(res)

# 맞음!
N = int(input())
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    temp = []
    for j in range(1, int(i**0.5)+1):
        temp.append(dp[i-j*j])
    dp[i] = min(temp) + 1
    print(temp)
print(dp[N])

# 다른 풀이 - 시간초과
N = int(input())
dp = [i for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[N])
