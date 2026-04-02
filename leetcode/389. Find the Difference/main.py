class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if t[0] == 1:
            return t[i]

        s = sorted(list(s))
        t = sorted(list(t))

        for i in range(len(t) - 1):
            if s[i] != t[i]:
                return t[i]

        return t[-1]
