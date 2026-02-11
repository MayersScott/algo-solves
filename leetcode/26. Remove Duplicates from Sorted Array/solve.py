class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expected_nums = list(set(nums))
        k = len(expected_nums)
        expected_nums.sort()
        ext = ['_'] * (len(nums) - k)
        expected_nums.extend(ext)
        nums[:] = expected_nums
        return k
