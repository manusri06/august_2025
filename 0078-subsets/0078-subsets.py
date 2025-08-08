class Solution(object):
    def subsets(self, nums):
        def rec(index):
            if index == len(nums):
                return [[]]
            s = rec(index+1)
            s1 = []
            for subset in s:
                s1.append([nums[index]]+subset)
            return s+s1
        return rec(0)

'''n = len(nums)
ans = []
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(nums[j])
    ans.append(subset)
return ans'''
        