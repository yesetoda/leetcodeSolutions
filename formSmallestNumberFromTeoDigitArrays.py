class Solution:
    def minNumber(nums1: list[int], nums2: list[int]) -> int:
        # l1 = sorted(nums1)[0]
        # l2 = sorted(nums2)[0]
        # both = 0
        # if len(nums1)>len(nums2):
        #     for i in nums2:
        #         if i in nums1:
        #             if i>both:
        #                 both=i
        # elif len(nums2)>len(nums1):
        #     for i in nums1:
        #         if i in nums2:
        #             if i>both:
        #                 both=i
        # # print(both,l1,l2,nums1,nums2)
        # if l1 in nums2 and l2 in nums1:
        #     return str(min(l1,l2))
        # elif l1 in nums2:
        #     return str(l1)
        # elif l2 in nums1:
        #     return str(l2)
        # l3 = sorted([i for i in (str(l1)+str(l2))])
        # return str(both)  if both !=0 and both<int("".join(l3)) else  "".join(l3)
        l1 = min(nums1)
        l2 = min(nums2)
        both = 10

        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1 and i > both:
                    both = i
        elif len(nums2) > len(nums1):
            for i in nums1:
                if i in nums2 and i > both:
                    both = i

        if l1 in nums2 and l2 in nums1:
            return min(l1, l2)
        elif l1 in nums2:
            return l1
        elif l2 in nums1:
            return l2

        l3 = sorted(list(str(l1) + str(l2)))
        return both if both != 0 and both < int("".join(l3)) else int("".join(l3))
    print(type(minNumber([6,4,3,7,2,1,8,5],nums2 =[6,8,5,3,1,7,4,2])))