class Solution:
    def permuteUnique( nums: list[int]) -> list[list[int]]:
        def backtrack(nums, path, used, result):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(nums, path, used, result)
                used[i] = False
                path.pop()

        nums.sort() 
        result = []
        used = [False] * len(nums)
        backtrack(nums, [], used, result)
        return result
    print(permuteUnique([1, 1, 3]))