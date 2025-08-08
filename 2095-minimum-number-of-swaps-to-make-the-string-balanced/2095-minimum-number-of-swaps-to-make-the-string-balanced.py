class Solution:
    def minSwaps(self, s: str) -> int:
        c = 0
        for i in s:
            if i is '[':
                c += 1
            else:
                if c > 0:
                    c -= 1
        return (c+1)//2