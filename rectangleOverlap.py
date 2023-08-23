class Solution:
    def isRectangleOverlap(rec1: list[int], rec2: list[int]) -> bool:
        # if  rec2[2]< rec1[2]  and  rec2[2]>rec1[0] or  rec2[0]< rec1[2]  and  rec2[0]>rec1[0]:
        #     return True
        # elif rec1[2]< rec2[2]  and  rec1[2]>rec2[0] or  rec1[0]< rec2[2]  and  rec1[0]>rec2[0]:
        #     return True
        # elif rec2[1]< rec1[1]  and  rec2[1]>rec1[3] or  rec2[3]< rec1[1]  and  rec2[0]>rec1[3]:
        #     return True
        # elif rec1[1]< rec2[1]  and  rec1[1]>rec2[3] or  rec1[3]< rec2[1]  and  rec1[0]>rec2[3]:
        #     return True
        # else:
        #     return False
        # if rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
        #     return False
        return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3])
    print(isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))
    
    