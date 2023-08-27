class Solution:
    def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
    #     aliceSum = sum(aliceSizes)
    #     bobSum = sum(bobSizes)
    #     for i in set(aliceSizes):
    #         for  j in set(bobSizes):
    #             if aliceSum+j-i == bobSum+i-j:
    #                 return [i,j]
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        aliceSet = set(aliceSizes)
        bobSet = set(bobSizes)
        targetDiff = (bobSum - aliceSum) // 2

        for i in aliceSet:
            if i + targetDiff in bobSet:
                return [i, i + targetDiff]
    print(fairCandySwap([1,3],[2]))