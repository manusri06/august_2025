class Solution(object):
    def generate(self, numRows):
        
        if numRows == 1:
            return [[1]]
        dp = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return list(dp)