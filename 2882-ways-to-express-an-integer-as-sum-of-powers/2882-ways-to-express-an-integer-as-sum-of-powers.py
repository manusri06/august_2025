class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        ans = []
        for i in range(1, n+1):
            p = i ** x
            if p <= n:
                ans.append(p)
            else:
                break

        dp = [0] * (n + 1)
        dp[0] = 1  

        for power in ans:
            for t in range(n, power - 1, -1):
                dp[t] = (dp[t] + dp[t - power]) % MOD

        return dp[n]