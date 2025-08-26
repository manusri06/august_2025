class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_d = 0
        best_area = 0
        for w, h in dimensions:
            d = w*w + h*h  
            area = w*h
            if d > best_d or (d == best_d and area > best_area):
                best_d = d
                best_area = area
        return best_area