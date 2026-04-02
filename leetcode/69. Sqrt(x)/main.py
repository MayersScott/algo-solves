class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2
        res = 0

        while l <= r:
            mid = (l + r) // 2
            sqirt = mid * mid

            if sqirt == x:
                return mid
            elif sqirt < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
