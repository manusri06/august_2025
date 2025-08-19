class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        seq = 0
        for i in nums:
            if i == 0:
                seq += 1
                c += seq
            else:
                seq = 0
        return c
            

