class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        dup = set()
        k = 10
        n = len(s)
        for i in range(n-k+1):
            sub = s[i:i+k]
            if sub in ans:
                dup.add(sub)
            else:
                ans.add(sub)
        return list(dup)