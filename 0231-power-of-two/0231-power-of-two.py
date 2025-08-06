class Solution(object):
    def isPowerOfTwo(self, n):
        return n>0 and n&(n-1) == 0 
'''if n <= 0:
    return False
elif n&(n-1) == 0:
    return True

return False'''