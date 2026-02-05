class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        result = (-1 if is_negative else 1) * int(str(x)[::-1])

        return result if result <= 2**31 -1 and result >= -2 ** 31 else 0
