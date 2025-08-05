class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        ans = []
        for i in range(1<<n):
            subset = []
            for j in range(n):
                if i & (1<<j):
                    subset.append(nums[j])
            ans.append(subset)
        return ans
        