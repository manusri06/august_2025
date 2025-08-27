class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = t = 0
        for i in nums:
            n = (n^i) & (~t)
            t = (t^i) & (~n)    
        return n

