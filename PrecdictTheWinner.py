class Solution:
    def predictTheWinner(nums: list[int]) -> bool:
        p1, p2 = 0, 0
        while nums:
            print(p1, p2)
            if len(nums) <= 3:
                p1 += max(nums[0], nums[-1])
                if len(nums) == 3:
                    p2 += nums[1]
            else:
                if nums[1] > nums[-2] and nums[1] > nums[0]:
                    p1 += nums.pop()
                else:
                    p1 += nums.pop(0)
        return p1 >= p2
    print(predictTheWinner(nums = [1,5,2]))