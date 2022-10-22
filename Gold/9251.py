from pprint import pprint
import sys
sys.stdin.readline

s1 = input()
s2 = input()

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
for a in range(len(s2)):
    for b in range(len(s1)):
        if s2[a] == s1[b]:
            dp[a + 1][b + 1] = dp[a][b] + 1
        else:
            dp[a + 1][b + 1] = max(dp[a + 1][b], dp[a][b + 1])

pprint(dp)
print(dp[-1][-1])