class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1  = nums1[:m]
        nums2 = nums2[:n]
        nums1.extend(nums2)
        nums1.sort()
        return nums1
    print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))