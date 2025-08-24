class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()  
        ans = []
        
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            ans.append(tuple(subset))  
        unique = set(ans)
        return [list(x) for x in unique]

