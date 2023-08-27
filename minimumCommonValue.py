class Solution:
    def getCommon(nums1: list[int], nums2: list[int]) -> int:
        out = sorted(list(set(nums1).intersection(set(nums2))))
        return out[0] if out else -1
    print(getCommon(nums1 = [1,3], nums2 = [2,4]))