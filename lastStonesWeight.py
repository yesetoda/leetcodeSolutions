class Solution:
    @staticmethod
    def lastStoneWeight(stones: list[int]) -> int:
        srt = sorted(stones)
        while len(srt) > 1:
            x1 = srt[-1]
            x2 = srt[-2]
            ind1 = srt.index(x1)
            ind2 = srt.index(x2)
            if x1 != x2:
                srt.pop(ind1)
                srt.pop(ind2)
                srt.append(x1 - x2)
            else:
                srt.pop(ind1)
                srt.pop(ind2)
            srt.sort()
        return srt[0] if srt else 0


    print(lastStoneWeight(stones = [1]))