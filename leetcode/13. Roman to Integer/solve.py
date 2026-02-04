class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        t = [1] * len(s)
        for i in range(len(s)):
            if i != len(s) - 1 and t[i] != 0 and d[s[i]] < d[s[i+1]]:
                res += d[s[i+1]] - d[s[i]]
                print(s[i], s[i+1])
                t[i+1] = 0
            elif t[i] != 0:
                res += d[s[i]]
                print(s[i])
    
        return res
