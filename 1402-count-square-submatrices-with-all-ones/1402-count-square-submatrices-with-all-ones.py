class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        s = 0
        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    dp[i][j] = matrix[i][j]
    
                else:
                    if matrix[i][j]:
                        dp[i][j] = min(dp[i][j-1] ,dp[i-1][j-1] ,dp[i-1][j])+1
                s += dp[i][j]
        return s