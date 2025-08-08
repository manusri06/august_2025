class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        p = [True]*n
        p[0] = p[1] = False
        c = 0
        for i in range(2,n):
            if p[i] == True:
                c += 1
                for j in range(i*i,n,i):
                    p[j] = False
        return c