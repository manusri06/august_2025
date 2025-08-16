class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        i = 0
        while ans > 0:
            ans = ans & (ans-1)
            i += 1
        return i
