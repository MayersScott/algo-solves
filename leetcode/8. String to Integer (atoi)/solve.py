class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i = 1

        result = 0
        imin, imax = -2**31, 2**31 - 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + (ord(s[i]) - ord('0'))
            if sign * result <= imin:
                return imin
            if sign * result >= imax:
                return imax
            i += 1

        return sign * result
