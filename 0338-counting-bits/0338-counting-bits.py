class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n+1):
            k = 0
            while i > 0:
                i = i &(i-1)
                k += 1
            ans.append(k)
        return ans
