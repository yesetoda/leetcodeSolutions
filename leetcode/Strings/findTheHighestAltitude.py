class Solution:
    def largestAltitude(gain: list[int]) -> int:
        out = [0]
        for i in gain:
            out.append(out[-1]+i)
        return max(out)
    print(largestAltitude(gain = [-5,1,5,0,-7]))