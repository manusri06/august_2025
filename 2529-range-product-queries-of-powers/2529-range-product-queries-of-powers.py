class Solution(object):
    def productQueries(self, n, queries):
        powers = []
        while n:
            x = n & -n
            powers.append(x)
            n -= x
        MOD = 10**9 + 7
        ans = []
        for l, r in queries:
            prod = 1
            for p in powers[l:r+1]:
                prod = (prod * p) % MOD
            ans.append(prod)
        return ans