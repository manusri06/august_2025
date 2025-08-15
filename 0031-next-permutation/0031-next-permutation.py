class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        p = -1
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                p = i-1
                break
        if p == -1:
            nums.reverse()
            return nums
        for i in range(n-1,p,-1):
            if nums[p] < nums[i]:
                nums[p] , nums[i] = nums[i] , nums[p]
                break

        nums[p+1:] = reversed(nums[p+1:])
        return nums