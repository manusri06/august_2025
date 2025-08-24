class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        k = 1
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k-=1
            while(k<0):
                if nums[l] == 0:
                    k+=1
                l+=1
            max_len = max(max_len,i-l)
        return max_len
