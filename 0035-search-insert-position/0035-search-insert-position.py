class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] < target:
                    ans = i+1
        return ans