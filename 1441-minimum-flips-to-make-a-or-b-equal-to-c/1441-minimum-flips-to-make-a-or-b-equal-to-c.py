class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count = 0
        while c > 0 or a>0 or b>0:
            if c&1:
                if not((a&1) | (b&1)):
                    count+=1
            else:
                if (a&1) & (b&1):
                    count += 2
                elif (a&1) | (b&1):
                    count+=1
            c = c>> 1
            a = a >> 1
            b = b >> 1
        return count





