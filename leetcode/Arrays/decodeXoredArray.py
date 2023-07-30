class Solution:
    def decode( encoded: list[int], first: int) -> list[int]:
        n = len(encoded) + 1
        arr = [first] + [0] * (n - 1)
        for i in range(1, n):
            arr[i] = encoded[i-1] ^ arr[i-1]
        return arr
    print(decode(encoded = [1,2,3], first = 1))