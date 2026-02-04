class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        best_l, best_r = 0, 1

        for i in range(n):

            dist = 0
            while i - dist >= 0 and i + dist < n and s[i - dist] == s[i + dist]:
                l = i - dist
                r = i + dist
                if r - l + 1 > best_r - best_l:
                    best_l, best_r = l, r + 1
                dist += 1

            dist = 1
            while i - dist >= 0 and i + dist - 1 < n and s[i - dist] == s[i + dist - 1]:
                l = i - dist
                r = i + dist - 1
                if r - l + 1 > best_r - best_l:
                    best_l, best_r = l, r + 1
                dist += 1

            dist = 1
            while i - dist + 1 >= 0 and i + dist < n and s[i - dist + 1] == s[i + dist]:
                l = i - dist + 1
                r = i + dist
                if r - l + 1 > best_r - best_l:
                    best_l, best_r = l, r + 1
                dist += 1

        return s[best_l:best_r]
