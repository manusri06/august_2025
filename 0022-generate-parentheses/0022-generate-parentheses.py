class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def rec(curr,open,close):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if open < n:
                rec(curr+'(',open+1,close)
            if close < open:
                rec(curr+')',open,close+1)
        rec("",0,0)
        return res
        