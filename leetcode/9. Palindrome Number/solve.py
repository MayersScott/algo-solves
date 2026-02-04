class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))):
            if list(str(x))[i] == list(str(x))[len(str(x))-i-1]:
                continue
            else:
                return False

        return True
