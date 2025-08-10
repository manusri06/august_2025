class Solution(object):
    def reorderedPowerOf2(self, n):
        sort = ''.join(sorted(str(n)))
        for i in range(31):
            new = ''.join(sorted(str(1 << i)))
            if sort == new:
                return True
        return False