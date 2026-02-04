class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]

        for i in range(len(first)):
            char = first[i]
            if char != last[i]:
                return first[:i]
        return first
