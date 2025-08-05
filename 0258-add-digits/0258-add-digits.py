class Solution(object):
    def addDigits(self, num):
        # 1+((n-1)mod 9)
        while num >= 10:
            return 1+((num-1)%9)
        return num
'''while num >= 10:
temp = 0
while num > 0:
    temp += num % 10
    num = num //10
num = temp
return num'''


