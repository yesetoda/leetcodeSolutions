class Solution:
    def rotate(nums: list[int], k: int) -> None:
        a = []
        a[:]= nums[::]
        return [a[-k+i] for i in range(len(nums))]
    print(rotate(nums = [-1,-100,3,99], k = 3))
        