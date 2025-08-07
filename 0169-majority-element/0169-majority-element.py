class Solution(object):
    def majorityElement(self, nums):
        c = 0
        res = 0
        for i in nums:
            if c == 0:
                res = i
            if res == i:
                c += 1
            else:
                c -= 1
        return res