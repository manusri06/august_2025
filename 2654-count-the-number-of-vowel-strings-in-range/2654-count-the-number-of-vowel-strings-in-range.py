class Solution(object):
    def vowelStrings(self, words, left, right):
        c = 0
        v = "aeiou"
        for i in range(left,right+1):
            w = words[i]
            if w[0] in v and w[-1] in v:
                c += 1
        return c