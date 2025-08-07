class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        c1 = c2 = 0
        e1 = e2 = None
        for i in nums:
            if e1 == i:
                c1 += 1
            elif e2 == i:
                c2 += 1
            elif c1 == 0:
                e1 = i
                c1 = 1
            elif c2 == 0:
                e2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        arr = []
        n = len(nums)
        if nums.count(e1) > n/3:
            arr.append(e1)
        if nums.count(e2) > n/3:
            arr.append(e2)
        return arr

                