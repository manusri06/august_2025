class Solution(object):
    def longestCommonPrefix(self, strs):
        pref = strs[0]
        x = len(pref)
        for i in strs[1:]:
            while pref != i[0:x]:
                x -= 1
                if x == 0:
                    return ""
                pref = pref[0:x]
        return pref


'''if not strs:
    return ""
r = ""
for i in range(len(strs[0])):
    w = strs[0][i]
    for j in strs:
        if i >= len(j) or j[i] != w:
            return r
    r += w
return r'''