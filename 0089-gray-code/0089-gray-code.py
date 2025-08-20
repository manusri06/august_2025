class Solution:
    def grayCode(self, n: int) -> List[int]:
        r = 2**n
        ans = []
        for i in range(r):
            ans.append(i^(i>>1))
        return ans