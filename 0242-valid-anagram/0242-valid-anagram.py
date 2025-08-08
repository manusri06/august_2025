class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in s:
            count[ord(i)-ord('a')] += 1
        for i in t:
            if count[ord(i)-ord('a')] == 0:
                return False
            count[ord(i)-ord('a')] -= 1
        return True
        

        