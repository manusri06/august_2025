class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2,3,5,7,11,13,17,19,23,29]
        ans = 0
        for i in range(left,right+1):
            c = 0
            while i != 0:
                i = i & (i-1)
                c += 1
            if c in prime:
                ans += 1
        return ans