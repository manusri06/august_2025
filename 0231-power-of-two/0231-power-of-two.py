class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        elif n&(n-1) == 0:
            return True
        else:
            return False