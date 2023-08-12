class Solution:
    def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        nums2_leng = len(nums2)
        out = []
        for i in nums1:
            if i not in nums2:
                out.append(-1)
            else:
                search_ind = nums2.index(i)+1
                while True:
                    if search_ind<nums2_leng  and nums2[search_ind]<=i :
                        search_ind+=1
                    elif search_ind<nums2_leng and  nums2[search_ind] > i :
                        out.append(nums2[search_ind])
                        break
                    else:
                        out.append(-1)
                        break
        return out
    print(nextGreaterElement(nums1 = [2,4,1], nums2 = [1,2,3,4]))



