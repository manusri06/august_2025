class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        r = ""
        for i in range(len(strs[0])):
            w = strs[0][i]
            for j in strs:
                if i >= len(j) or j[i] != w:
                    return r
            r += w
        return r