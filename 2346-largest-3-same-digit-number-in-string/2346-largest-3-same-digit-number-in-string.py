class Solution(object):
    def largestGoodInteger(self, num):
        res = ""
        for i in range(1,len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                a = num[i-1:i+2]
                if a > res:
                    res = a
        return res