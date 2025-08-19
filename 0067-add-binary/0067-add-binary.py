class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = j = carry = 0
        ans = ""
        al = len(a)
        bl = len(b)
        while i<al or j<bl or carry:
            A = int(a[al-i-1]) if i<al else 0
            B = int(b[bl-i-1]) if j<bl else 0

            s = A+B+carry
            ans = str(s%2)+ans
            carry = s//2
            i+=1
            j+=1
        return ans