class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = "1"
        for i in range(2,n+1):
            res = ""
            count = 1
            for i in range(1,len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    res += str(count)+prev[i-1]
                    count = 1
            res += str(count)+prev[-1]
            prev = res
        return prev