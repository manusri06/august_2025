class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        
        x = len(nums)
        d = x//2
        if x%2 == 0:
            return (nums[d] + nums[d-1])/2.0
        else:
            return (nums[d])
