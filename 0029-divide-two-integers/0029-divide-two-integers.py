class Solution(object):
    def divide(self, dividend, divisor):
        def d(dividend, divisor):
            s = 0
            i = 0
            if dividend == 0:
                return s
            while (divisor << i) <= dividend:
                i += 1
            if i > 0:
                s = s + (1<<(i-1))
                dividend -= divisor << (i-1)
                s += d(dividend,divisor)
            return s

        numer = dividend < 0
        deno = divisor < 0 
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        if numer ^ deno:
            sign = -1
        else:
            sign = 1
        return sign*d(abs(dividend),abs(divisor))
        

    

'''if dividend == -2**31 and divisor == -1:
    return (2**31) - 1 

i = 0
while abs(dividend) >= abs(divisor):
    abs(dividend) -= abs(divisor)
    i += 1

if dividend <0 or divisor < 0:
    return -i
else:
    return i'''