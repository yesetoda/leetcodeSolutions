class Solution:
    def maxDistance(nums1: list[int], nums2: list[int]) -> int:
        valid = []
        for i in range(len(nums1)):
            for j in range(i,len(nums2)):
                if nums1[i]<=nums2[j]:
                    print(i,j)
                    valid.append(j-i)
        return sorted(valid)[-1]
    print(maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))