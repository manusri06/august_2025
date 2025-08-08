class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def rec(start,curr,total):
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return
            for i in range(start,len(candidates)):
                curr.append(candidates[i])
                rec(i,curr,total+candidates[i])
                curr.pop()
        rec(0,[],0)
        return res
        