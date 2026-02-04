class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res_list = nums1 + nums2
        res_list.sort()

        n = len(res_list)
        
        print(res_list)

        if not n % 2 and n > 2:
            print(res_list[n//2], res_list[n//2 + 1])
            return (res_list[n//2] + res_list[n//2 - 1]) / 2
        elif n == 2:
            print(res_list[0], res_list[1])
            return (res_list[0] + res_list[1]) / 2
        else:
            return res_list[n//2]
