class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        i = j = 0
        ans = []
        direction = 1  

        while len(ans) < row * col:
            ans.append(mat[i][j])

            if direction == 1:   
                if j == col - 1:     
                    i += 1
                    direction = -1
                elif i == 0:         
                    j += 1
                    direction = -1
                else:                 
                    i -= 1
                    j += 1

            else:   
                if i == row - 1:      
                    j += 1
                    direction = 1
                elif j == 0:          
                    i += 1
                    direction = 1
                else:                 
                    i += 1
                    j -= 1

        return ans