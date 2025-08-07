class Solution(object):
    def rotate(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        j = 0
        for i in range(r):
            for j in range(i+1,c):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in matrix:
            i[:] = i[::-1]
        return matrix
        