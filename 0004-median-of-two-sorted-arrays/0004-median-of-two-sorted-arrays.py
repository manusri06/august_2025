class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        x = len(nums)
        d = x//2
        if x%2 == 0:
            return (nums[d] + nums[d-1])/2.0
        else:
            return (nums[d])
