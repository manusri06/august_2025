class Solution(object):
    def threeSumClosest(self, nums, target):
        num = sorted(nums)
        n = len(num)
        res = float('inf')
        for i in range(n-2):
            l , r = i+1 , n-1
            while l < r:
                c_sum = num[i]+num[l]+num[r]
                if abs(c_sum - target) < abs(res - target):
                    res = c_sum
                if c_sum < target:
                    l += 1
                elif c_sum > target:
                    r -= 1
                else:
                    return c_sum
        return res
