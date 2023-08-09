class Solution:
    def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        mid =len(nums1)//2
        if len(nums1)%2 ==0:
            return float((nums1[mid-1]+nums1[mid])/2)
        else:
            return float(nums1[mid])

    print(findMedianSortedArrays( nums1 = [], nums2 = [3,4]))