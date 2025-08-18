class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        next_nums = []
                        for k in range(n):
                            if k != i and k != j:
                                next_nums.append(nums[k])

                       
                        for val in self.compute(nums[i], nums[j]):
                            if solve(next_nums + [val]):
                                return True
            return False

        return solve(cards)

    def compute(self, a, b):
        results = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:
            results.append(a / b)
        if abs(a) > 1e-6:
            results.append(b / a)
        return results
