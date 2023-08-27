class Solution:
    def mergeArrays( nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        s = set([i[0] for i in nums1])
        for i in nums2:
            s.add(i[0])
        sm = {i:0 for i in s}
        for i in nums1:
            sm[i[0]] +=i[1]
        for j in nums2:
            sm[j[0]] +=j[1]
        out = []
        for i in sm.items():
            out.append([i[0],i[1]])

        return sorted(out)
    print(mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))