class Solution:
    def minOperations( boxes: str) -> list[int]:
        boxes = [int(i) for i in boxes]
        out = [0 for i in  range(len(boxes))]
        for i in  range(len(boxes)):
            for j in  range(len(boxes)):
                if i == j:
                    pass
                else:
                    out[i] += boxes[j]*abs(i-j)
        return out
    print(minOperations(boxes = "001011"))
        